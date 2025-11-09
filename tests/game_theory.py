import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import random

class PrisonersDilemmaGame:
    """囚徒困境游戏环境"""
    
    def __init__(self):
        # 收益矩阵 (合作=0, 背叛=1)
        # 格式: [玩家1行动, 玩家2行动] -> [玩家1收益, 玩家2收益]
        self.payoff_matrix = {
            (0, 0): (3, 3),  # 都合作 (CC)
            (0, 1): (0, 5),  # 玩家1合作，玩家2背叛 (CD)
            (1, 0): (5, 0),  # 玩家1背叛，玩家2合作 (DC)
            (1, 1): (1, 1)   # 都背叛 (DD) - 纳什均衡
        }
        
    def get_payoffs(self, action1, action2):
        """获取双方收益"""
        return self.payoff_matrix[(action1, action2)]
    
    def get_nash_equilibrium(self):
        """纳什均衡: 都背叛 (1, 1)"""
        return (1, 1)
    
    def get_pareto_optimal(self):
        """帕累托最优: 都合作 (0, 0)"""
        return (0, 0)

class QLearningAgent:
    """Q-learning智能体"""
    
    def __init__(self, agent_id, learning_rate=0.1, discount_factor=0.95, 
                 exploration_rate=1.0, exploration_decay=0.995, min_exploration=0.01):
        self.agent_id = agent_id
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.epsilon_decay = exploration_decay
        self.min_epsilon = min_exploration
        
        # Q表: 状态 -> 动作值
        # 这里状态是对手的历史动作
        self.q_table = defaultdict(lambda: [0.0, 0.0])  # [合作值, 背叛值]
        
        # 历史记录
        self.action_history = []
        self.reward_history = []
        
    def get_state(self, opponent_history, window_size=3):
        """根据对手历史动作构建状态"""
        if len(opponent_history) < window_size:
            return tuple(opponent_history + [0] * (window_size - len(opponent_history)))
        return tuple(opponent_history[-window_size:])
    
    def choose_action(self, state):
        """选择动作 (epsilon-greedy策略)"""
        if random.random() < self.epsilon:
            return random.choice([0, 1])  # 随机探索
        else:
            q_values = self.q_table[state]
            return np.argmax(q_values)  # 贪婪选择
    
    def update_q_table(self, state, action, reward, next_state):
        """更新Q表"""
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state])
        
        # Q-learning更新公式
        new_q = current_q + self.lr * (reward + self.gamma * next_max_q - current_q)
        self.q_table[state][action] = new_q
    
    def decay_exploration(self):
        """衰减探索率"""
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)
    
    def get_cooperation_probability(self, opponent_history):
        """获取合作概率"""
        state = self.get_state(opponent_history)
        q_values = self.q_table[state]
        if q_values[0] == q_values[1]:
            return 0.5
        return 1.0 if q_values[0] > q_values[1] else 0.0

class ExperimentRunner:
    """实验运行器"""
    
    def __init__(self, num_episodes=10000):
        self.game = PrisonersDilemmaGame()
        self.num_episodes = num_episodes
        
        # 创建两个智能体
        self.agent1 = QLearningAgent(1)
        self.agent2 = QLearningAgent(2)
        
        # 记录实验数据
        self.cooperation_rates = []
        self.payoffs_history = []
        self.nash_distances = []
        
    def run_experiment(self):
        """运行实验"""
        print("开始强化学习实验...")
        
        for episode in range(self.num_episodes):
            # 获取当前状态
            state1 = self.agent1.get_state(self.agent2.action_history)
            state2 = self.agent2.get_state(self.agent1.action_history)
            
            # 智能体选择动作
            action1 = self.agent1.choose_action(state1)
            action2 = self.agent2.choose_action(state2)
            
            # 获取收益
            payoff1, payoff2 = self.game.get_payoffs(action1, action2)
            
            # 记录动作和收益
            self.agent1.action_history.append(action1)
            self.agent2.action_history.append(action2)
            self.agent1.reward_history.append(payoff1)
            self.agent2.reward_history.append(payoff2)
            
            # 获取下一状态
            next_state1 = self.agent1.get_state(self.agent2.action_history)
            next_state2 = self.agent2.get_state(self.agent1.action_history)
            
            # 更新Q表
            self.agent1.update_q_table(state1, action1, payoff1, next_state1)
            self.agent2.update_q_table(state2, action2, payoff2, next_state2)
            
            # 衰减探索率
            self.agent1.decay_exploration()
            self.agent2.decay_exploration()
            
            # 记录统计数据
            if episode % 100 == 0:
                self._record_statistics(episode)
                
        print("实验完成!")
        return self._get_results()
    
    def _record_statistics(self, episode):
        """记录统计数据"""
        # 计算最近100轮的合作率
        recent_actions1 = self.agent1.action_history[-100:]
        recent_actions2 = self.agent2.action_history[-100:]
        
        if len(recent_actions1) > 0:
            cooperation_rate = (recent_actions1.count(0) + recent_actions2.count(0)) / (2 * len(recent_actions1))
            self.cooperation_rates.append(cooperation_rate)
            
            # 计算平均收益
            recent_payoffs1 = self.agent1.reward_history[-100:]
            recent_payoffs2 = self.agent2.reward_history[-100:]
            avg_payoff = (np.mean(recent_payoffs1) + np.mean(recent_payoffs2)) / 2
            self.payoffs_history.append(avg_payoff)
            
            # 计算与纳什均衡的距离
            nash_action = self.game.get_nash_equilibrium()
            current_strategy = (
                1 - self.agent1.get_cooperation_probability(self.agent2.action_history),
                1 - self.agent2.get_cooperation_probability(self.agent1.action_history)
            )
            nash_distance = np.sqrt(sum((a - b)**2 for a, b in zip(current_strategy, nash_action)))
            self.nash_distances.append(nash_distance)
    
    def _get_results(self):
        """获取实验结果"""
        final_coop_prob1 = self.agent1.get_cooperation_probability(self.agent2.action_history)
        final_coop_prob2 = self.agent2.get_cooperation_probability(self.agent1.action_history)
        
        nash_equilibrium = self.game.get_nash_equilibrium()
        pareto_optimal = self.game.get_pareto_optimal()
        
        results = {
            'final_cooperation_probs': (final_coop_prob1, final_coop_prob2),
            'final_defection_probs': (1 - final_coop_prob1, 1 - final_coop_prob2),
            'nash_equilibrium': nash_equilibrium,
            'pareto_optimal': pareto_optimal,
            'converged_to_nash': abs(1 - final_coop_prob1 - nash_equilibrium[0]) < 0.1 and 
                               abs(1 - final_coop_prob2 - nash_equilibrium[1]) < 0.1,
            'total_episodes': self.num_episodes,
            'final_cooperation_rate': self.cooperation_rates[-1] if self.cooperation_rates else 0,
            'final_average_payoff': self.payoffs_history[-1] if self.payoffs_history else 0
        }
        
        return results

def visualize_results(runner, results):
    """可视化实验结果"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('囚徒困境中的强化学习与纳什均衡分析', fontsize=16, fontweight='bold')
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 1. 合作率演化
    axes[0, 0].plot(runner.cooperation_rates, linewidth=2, color='blue')
    axes[0, 0].set_title('合作率随训练进程的变化')
    axes[0, 0].set_xlabel('训练步数 (×100)')
    axes[0, 0].set_ylabel('合作率')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(y=0.5, color='red', linestyle='--', alpha=0.7, label='随机策略')
    axes[0, 0].axhline(y=0.0, color='orange', linestyle='--', alpha=0.7, label='纳什均衡')
    axes[0, 0].axhline(y=1.0, color='green', linestyle='--', alpha=0.7, label='帕累托最优')
    axes[0, 0].legend()
    
    # 2. 平均收益演化
    axes[0, 1].plot(runner.payoffs_history, linewidth=2, color='green')
    axes[0, 1].set_title('平均收益随训练进程的变化')
    axes[0, 1].set_xlabel('训练步数 (×100)')
    axes[0, 1].set_ylabel('平均收益')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axhline(y=1, color='orange', linestyle='--', alpha=0.7, label='纳什均衡收益')
    axes[0, 1].axhline(y=3, color='blue', linestyle='--', alpha=0.7, label='帕累托最优收益')
    axes[0, 1].legend()
    
    # 3. 与纳什均衡的距离
    axes[1, 0].plot(runner.nash_distances, linewidth=2, color='red')
    axes[1, 0].set_title('策略与纳什均衡的距离')
    axes[1, 0].set_xlabel('训练步数 (×100)')
    axes[1, 0].set_ylabel('欧几里得距离')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='orange', linestyle='--', alpha=0.7, label='纳什均衡')
    axes[1, 0].legend()
    
    # 4. 最终策略热力图
    strategies = np.array([
        [results['final_cooperation_probs'][0], 1 - results['final_cooperation_probs'][0]],
        [results['final_cooperation_probs'][1], 1 - results['final_cooperation_probs'][1]]
    ])
    
    im = axes[1, 1].imshow(strategies, cmap='RdYlBu', aspect='auto', vmin=0, vmax=1)
    axes[1, 1].set_title('最终策略矩阵')
    axes[1, 1].set_xticks([0, 1])
    axes[1, 1].set_xticklabels(['合作', '背叛'])
    axes[1, 1].set_yticks([0, 1])
    axes[1, 1].set_yticklabels(['智能体1', '智能体2'])
    
    # 添加数值标签
    for i in range(2):
        for j in range(2):
            text = axes[1, 1].text(j, i, f'{strategies[i, j]:.3f}',
                                 ha="center", va="center", color="black", fontweight='bold')
    
    plt.colorbar(im, ax=axes[1, 1], label='概率')
    plt.tight_layout()
    plt.show()

def print_analysis(results):
    """打印分析结果"""
    print("\n" + "="*60)
    print("实验结果分析")
    print("="*60)
    
    print(f"训练轮数: {results['total_episodes']:,}")
    print(f"纳什均衡 (都背叛): {results['nash_equilibrium']}")
    print(f"帕累托最优 (都合作): {results['pareto_optimal']}")
    
    print(f"\n最终策略:")
    print(f"智能体1 - 合作概率: {results['final_cooperation_probs'][0]:.3f}, 背叛概率: {results['final_defection_probs'][0]:.3f}")
    print(f"智能体2 - 合作概率: {results['final_cooperation_probs'][1]:.3f}, 背叛概率: {results['final_defection_probs'][1]:.3f}")
    
    print(f"\n收敛性分析:")
    print(f"是否收敛到纳什均衡: {'是' if results['converged_to_nash'] else '否'}")
    print(f"最终合作率: {results['final_cooperation_rate']:.3f}")
    print(f"最终平均收益: {results['final_average_payoff']:.3f}")
    
    # 理论分析
    print(f"\n理论分析:")
    print("纳什均衡预测: 两个智能体都应该选择背叛")
    print("实际结果:", end=" ")
    if results['converged_to_nash']:
        print("✓ 智能体收敛到纳什均衡，符合博弈论预测")
    else:
        print("✗ 智能体未完全收敛到纳什均衡")
        if results['final_cooperation_rate'] > 0.5:
            print("  → 智能体表现出合作倾向，可能受到重复博弈效应影响")
        else:
            print("  → 智能体倾向于背叛，但尚未完全收敛")

# 运行实验
def main():
    # 创建实验运行器
    runner = ExperimentRunner(num_episodes=10000)
    
    # 运行实验
    results = runner.run_experiment()
    
    # 打印分析结果
    print_analysis(results)
    
    # 可视化结果
    visualize_results(runner, results)
    
    return runner, results

# 执行主函数
if __name__ == "__main__":
    runner, results = main()
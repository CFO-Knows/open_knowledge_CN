# QBO注册及月度bookkeeping流程

Quickbooks里有两套世界：

* 银行页 bank feed，银行和信用卡流水，没入账
* 账簿 books、GL、reports，已入账的entries、报表，由会计逻辑提供

为什么要分开呢？因为银行显示1000出账，系统无法确定：

* 还信用卡？
* 付给供应商？
* 老板提取？
* 买设备？

所以他不能立刻入账，必须由人（bookkeeper或企业主自己）点：

* match：对上已有交易，不产生新的entries
* add：新增交易
* record as transfer：创建或确认一笔账户间转账
* exclude：忽略，不入账

一般来说，企业主不会自己去match或者add，这个一般由bookkeeper来完成。企业主只关心经营数据。

QBO不会自动创建entries，除非你设置了规则。QBO会：

* 自动识别对方名称、金额、描述
* 提出智能建议，比如：看起来像上次的google ads付款，要不要分类为广告费？
* 但仍要人工点击确认

QBO的这种方式可以防止出错，同时节省人力

本页介绍一个一般的小型企业如何注册QBO并由bookkeeper完成一个常规的月度bookkeeping。

## 注册新账号

### 基本信息采集

![1762612284298](image/QBO注册引导/1762612284298.png)

![1762612292472](image/QBO注册引导/1762612292472.png)

![1762612300903](image/QBO注册引导/1762612300903.png)

![1762612316392](image/QBO注册引导/1762612316392.png)

![1762612330113](image/QBO注册引导/1762612330113.png)

![1762612340351](image/QBO注册引导/1762612340351.png)

![1762612355339](image/QBO注册引导/1762612355339.png)

这里有三个分流，我们按顺序看：

### invoice设置

invoice个性化设置

这里要注意这里的invoice指的是customer invoice，也就是收款发票；付款在QBO中叫做bill, vendor invoice以及支付款项的receipes。

这里要开通线上收款功能，可以让收到invoice的商家直接支付，同时quickbooks也可以记录

![1762612394443](image/QBO注册引导/1762612394443.png)

![1762612402705](image/QBO注册引导/1762612402705.png)

![1762612413073](image/QBO注册引导/1762612413073.png)

![1762612464902](image/QBO注册引导/1762612464902.png)

![1762612473470](image/QBO注册引导/1762612473470.png)

![1762612494920](image/QBO注册引导/1762612494920.png)

![1762612517167](image/QBO注册引导/1762612517167.png)

这里因为是虚设，所以暂先跳过

![1762612537911](image/QBO注册引导/1762612537911.png)

### payroall

![1762612556569](image/QBO注册引导/1762612556569.png)

### bank connecting

![1762612590312](image/QBO注册引导/1762612590312.png)

![1762612598801](image/QBO注册引导/1762612598801.png)

![1762612605927](image/QBO注册引导/1762612605927.png)

右上角关闭，暂且skip

### receipts

![1762612643230](image/QBO注册引导/1762612643230.png)

这个就是说用手机app实现随时随地拍照保存receipts，QuickBooks 会自动将你拍的收据与相应的支出记录匹配，这样你就可以轻松追踪开销并在报税时节省时间和税款。

**功能用途总结：**

这一步的目的在于让你下载 QuickBooks 的手机 App，这样你就可以：

1. 拍下纸质收据（比如餐饮、办公用品发票等）；
2. QuickBooks 会自动识别金额、商家名称、日期等信息；
3. 自动把这些支出分类、录入到你的账本中；
4. 帮助你记录费用、生成报表、以及报税时抵扣。

### 最后的用途或者其他常规询问

![1762612917269](image/QBO注册引导/1762612917269.png)

![1762612926935](image/QBO注册引导/1762612926935.png)

![1762612931865](image/QBO注册引导/1762612931865.png)

这里展示一些动画，之后就设置完成进入到了主页面

### 第一次进入主页面

第一次进入主页面会有一系列的引导：

![1762612984442](image/QBO注册引导/1762612984442.png)

![1762613004929](image/QBO注册引导/1762613004929.png)

![1762613015071](image/QBO注册引导/1762613015071.png)![1762613023476](image/QBO注册引导/1762613023476.png)

![1762613030174](image/QBO注册引导/1762613030174.png)

右侧会弹出一个tasks任务窗口，可以看到要做的任务

![1762613134178](image/QBO注册及操作界面/1762613134178.png)

这个步骤在AI系统中应当由agent直接像人一样不断提问或者喂过来。

## Import and Match Transactions

![1762562937891](image/QBO/1762562937891.png)

### 两种导入方式

#### 链接银行自动导入

连接银行，link bank，read only access只能查账

#### 手动上传文件导入

如果不能连接银行，也可以upload transactions，导入的格式包括csv，qfx，qbo，ofx，或者txt；导入的时候要选择transactions发生的账户

csv中的文件有以下这些：

![1762563328416](image/QBO/1762563328416.png)

手动导入的时候需要手动填写csv的内容：

![1762563431334](image/QBO/1762563431334.png)

手动导入后，需要选择要添加的transactions：

![1762563492527](image/QBO/1762563492527.png)

![1762563506248](image/QBO/1762563506248.png)

添加完成后：

![1762563525102](image/QBO/1762563525102.png)

### 配对信用卡还款交易

![1762563717830](image/QBO/1762563717830.png)

![1762563733050](image/QBO/1762563733050.png)

这里其实就是说Quickbooks检测到：

* 你的银行账户有一笔支出
* 你的信用卡账户有一笔金额相同的入账

Quickbooks识别出这两笔交易是同一件事的两面：一个支出、一个入账，于是提示你去确认配对；配对后，这笔还款会在账本中正确反映为从银行账户转出资金到信用卡的动作，而不会重复计算。

为什么这里要进行该动作呢？因为公司通常会给员工或管理层发放公司信用卡，用于支付公司费用，比如差旅费、机票、酒店、设备采购、广告支出、SaaS订阅等。这些刷卡消费都是公司开支，而每个月公司都会从公司的银行账户（比如BOA）中去还这张信用卡。

由于跨越还款非常常见，所以一般会这样记录：

在刷信用卡的当下，公司已经发生了费用，所以要立即入账：

| 日期  | 账户                              | 借方（Debit） | 贷方（Credit） |
| ----- | --------------------------------- | ------------- | -------------- |
| 10/25 | 费用（Advertising Expense）       | $1,000        |                |
| 10/25 | 信用卡负债（Credit Card Payable） |               | $1,000         |

意思是：公司花了 $1,000 做广告，但这笔钱暂时由信用卡垫付，公司还欠银行这笔钱。

下个月还款的时候，记录偿还负债：

| 日期  | 账户                              | 借方（Debit） | 贷方（Credit） |
| ----- | --------------------------------- | ------------- | -------------- |
| 11/10 | 信用卡负债（Credit Card Payable） | $1,000        |                |
| 11/10 | 银行账户（Bank Checking）         |               | $1,000         |

意思是：用银行账户的钱偿还信用卡负债，不影响利润，因为费用早在刷卡时已确认。

在 QuickBooks 中：

* 10月刷卡 → 这笔会出现在“信用卡账户（Credit Card Account）”中作为支出。
* 11月还款 → 会出现在“银行账户（Bank Account）”中作为转出。
* 系统会帮你把两笔连接（match）起来，作为偿还信用卡负债的内部转账（Transfer）。

系统match两笔entries后，entries记录和总账不变，那么match的意义是什么？

我们来回顾一下刚才的流程，首先我们从银行流水中下载transactions，这些transactions会形成bank feed rows（待处理行）：此时这些transactions还没有入账。只有当你在银行页点击match、confirm、add、record as transfer时，才会把待处理行变成账上的一笔交易。如果你不点，那么就不会入账。

### 手动创建和录入Journal Entry

在会计理论中，Journal Entry就是会计分录，是所有交易记录的基础形式。具体来说，journal entry是double entries的一条记录。

在QBO中，Journal Entry是一个功能，让你手动创建或调整会计分录的。

手动录入一笔借贷平衡的交易。它是最基础、最通用的会计记录方式，用来记录**没有自动交易来源**的财务事项。在 QuickBooks 里，很多交易是自动生成分录的（比如发票、收据、费用、银行匹配等），但有时你需要手动调整账户余额，就用 Journal Entry功能（在QBO中是一个独立的功能）。

例如：你用个人钱帮公司付了 500 元办公用品费，但没通过公司银行账户。在 QuickBooks 里可以这样做：

| 科目                                             | 借方（Dr） | 贷方（Cr） |
| ------------------------------------------------ | ---------- | ---------- |
| Office Supplies（办公用品费）                    | 500        |            |
| Owner’s Equity / Owner Contribution（业主投入） |            | 500        |

。

### Petty Cash

**Petty Cash（备用金）** 是公司手头的一小笔现金，用来支付一些小额、临时开销。

比如：

* 打印机墨盒、文具
* 快递费、停车费
* 小额补贴等

这些不值得每次都跑银行取钱或开支票，所以公司会留一点现金备用。

**在 QuickBooks 中怎么处理 Petty Cash：**

1. **建立账户**
   * 打开 **Accounting → Chart of Accounts → New**
   * Account Type 选 **Cash and cash equivalents**
   * Detail Type 选 **Petty Cash**
   * 命名为 “Petty Cash” 或 “备用金账户”
2. **资金来源**
   * 当你从银行取出现金备用时，做一笔 Transfer：
     * From: Bank Account
     * To: Petty Cash
     * 金额：比如 $200

       👉 这表示你取了 200 元现金放在抽屉里。
3. **支出时**
   * 发生小额支出（如打车费 30 元）：
     * 用 Petty Cash 账户创建一笔 Expense。
4. **现金用完再补充**
   * 再从银行转一笔钱到 Petty Cash。

💬 最终效果：

Petty Cash 就像一个小型“现金钱包”，在账上独立核算、透明记录。

---

举例来说：

🪙 **Scenario 1: Withdraw cash from bank to create Petty Cash fund**

**Situation:**

You withdraw **$200** from the company bank account and keep it as petty cash.

**Journal Entry:**

| Account      | Debit | Credit |
| ------------ | ----- | ------ |
| Petty Cash   | $200  |        |
| Bank Account |       | $200   |

**Explanation:**

* You moved money **from** your bank (decrease)
* **to** your petty cash (increase).
* Total assets didn’t change — only their form changed (bank → cash).

---

🧾 **Scenario 2: Use petty cash to pay for office supplies**

**Situation:**

You pay **$50** in cash for office supplies (pens, paper, etc.) using the petty cash fund.

**Journal Entry:**

| Account                 | Debit | Credit |
| ----------------------- | ----- | ------ |
| Office Supplies Expense | $50   |        |
| Petty Cash              |       | $50    |

**Explanation:**

* The **Office Supplies Expense** increases (debit = expense up).
* **Petty Cash** decreases (credit = cash down).
* This reflects you spent cash on a business expense.

---

💵 **Scenario 3: Replenish the petty cash fund**

**Situation:**

You notice only $150 cash is left, so you withdraw another **$100** from the bank to top it back up to $250 total.

**Journal Entry:**

| Account      | Debit | Credit |
| ------------ | ----- | ------ |
| Petty Cash   | $100  |        |
| Bank Account |       | $100   |

**Explanation:**

* Petty Cash increases by $100 (you physically added more bills).
* Bank Account decreases by $100 (you withdrew from it).

### Bank Feed总结

![1762713291174](image/QBO/1762713291174.png)









## 月末对账

在美国，小企业大多数使用“Calendar Year”（自然年）：

* 每个月做账 Monthly Closing
* 每季度报税 Quarterly Taxes
* 每年报年度报表 Annual Report

所以Quickbooks默认以自然月为周期，月末会让你：

* 对账 Reconcile
* 生成月度利润表 P&L
* 生成资产负债表 Balance Sheet

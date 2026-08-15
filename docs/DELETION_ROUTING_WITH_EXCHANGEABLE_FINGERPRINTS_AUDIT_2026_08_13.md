# State-dependent placement 的删除 routing：可交换 fingerprint 与固定状态障碍

> 日期：2026-08-13。状态：本文给出一个严格的 routing-elimination lemma，说明
> cuckoo-like placement 不一定要保存 per-key orientation；同时证明最直接的
> fixed-slot realization仍不能给所需 zero-overflow upper bound。没有宣称文献
> 中尚未核实的 exact constant。

## 1. 模型与空间账本

目标是 ordinary dynamic AMQ：容量 (n)，固定 (arepsilon=1/2)，固定长度
persistent state，任意长合法 key-only history，zero false negatives，pointwise
FPR，无外部 exact set 或 rebuild oracle。公共随机 tape 免费，但所有 placement、
stash、overflow、epoch 和 routing metadata 必须计入状态。

对 cuckoo-style候选，一个 key (x) 公开得到：

\[
i_1(x)\in[B],
\qquad f(x)\in[2^r],
\qquad i_2(x)=i_1(x)\oplus g(f(x)).
\tag{1}
\]

每 bucket 有 (b) 个 slots。slot 保存 occupied bit 与 (r)-bit fingerprint；query
检查两个 buckets 中是否存在匹配 fingerprint。

完整空间必须分为：

\[
H=H_{\rm slots}+H_{\rm occupancy}+H_{\rm stash}
+H_{\rm overflow}+H_{\rm seeds}+H_{\rm aux}.
\tag{2}

公共 fully random tape 不计 seeds；但若结构为解决某个 instance 选择 seed，选择
结果必须计费。

## 2. Per-key orientation 可以严格消除

### Theorem 2.1（exchangeable-fingerprint deletion routing）

假设候选 bucket pair 满足式 (1)，并且 persistent state 只保存每个 occupied slot
的 fingerprint，不保存 key identity。允许任意 state-dependent relocations，但每个
fingerprint copy始终位于其两个合法 buckets之一。

`Delete(x)` 读取 (i_1(x),i_2(x),f(x))，并在这两个 buckets 中删除任意一个
fingerprint 等于 (f(x)) 的 slot。若 update promise 保证 (x) 当前存在，则该
操作不会造成 false negative，即使删掉的 physical copy不是插入 (x) 时创建的
copy。因此不需要保存每个 key 的 orientation bit。

**证明。** 设某个 slot 在 bucket (j\in\{i_1(x),i_2(x)}) 中保存 fingerprint
(f(x))，它来自当前 key (y)。由 alternate bucket rule，若
(i_1(y)=j)，则另一候选是 (j\oplus g(f(y)))；若 (i_2(y)=j)，另一候选仍为
(j\oplus g(f(y)))。因为 (f(y)=f(x))，unordered candidate pair恰等于
(x) 的 pair。故这两个 keys 在 AMQ state 中完全可交换。

删除任一匹配 copy 后，candidate pair 内 fingerprint (f(x)) 的 slot multiplicity
减少一。合法 delete 保证删除前至少有一个代表 (x) 的 copy；即使实际删的是
(y) 的 copy，剩余代表总数仍等于剩余 keys 数。每个剩余同类 key query同一 pair
且看到同一 fingerprint，所以没有 false negative。证毕。

这个 lemma 同时处理 duplicate fingerprints 与 relocations。它推翻了“adaptive
placement 必然每 key 支付一个 choice bit”的过强说法。真正 routing unit 是

\[
(\text{unordered bucket pair},\text{fingerprint})
\]

的 exchangeability class，而不是 key identity。

## 3. FPR 与理想 slot 账本

若总 slots 为 (M=s n)，每 bucket (b) slots，则 query检查至多 (2b) 个
fingerprints。忽略 bucket相关性，标准 union bound 给

\[
\varepsilon\le\frac{2b}{2^r}.
\tag{3}
\]

要达到 (arepsilon=1/2)，最小整数 fingerprint bits 满足

\[
r\ge\lceil\log_2(4b)\rceil.
\tag{4}

若用 fixed slots 显式存 occupancy，粗空间是

\[
H_{\rm raw}=M(r+1)=sn(r+1),
\]

通常明显超过 (2.349n)。若 occupancy pattern enumeratively编码，在恰有至多
(n) 个 occupied slots时，理想账本为

\[
\frac Hn
\approx r+s,h_2(1/s).
\tag{5}

式 (5) 故意没有加入 stash/overflow。即使把 load factor允许到极激进水平，
整数 (r,b) 的直接优化也没有产生可信的 (<2.349) zero-overflow参数；更重要的
是下一节的 fixed-state障碍使这种平均-load计算不能直接成为 theorem。

## 4. Fixed-state / arbitrary-history 障碍

Standard cuckoo placement只在随机 candidate graph 可 orient 到 bucket capacities时
成功。对 fixed set，失败概率可以很小；对 polynomial oblivious sequence，可用
stash、rehash或 rebuild得到 whp保证。这些都不等于当前模型要求的：

- 每条 tape 上固定 (H)-bit state space；
- 任意长合法 history；
- 永不 overflow；
- 无外部 exact set帮助 rebuild。

对某些 tape，universe 中可能存在超过 (2b) 个 keys 具有同一 unordered bucket
pair，而合法 history可同时插入其中 (n) 个。若 fingerprints也相同，该 pair的
(2b) slots无法容纳所有 copies。AMQ 虽不需要区分 identities，但 key-only合法
deletion要求代表 multiplicity至少能经任意长 insert/delete cycles正确增减；单个
presence bit会重现 last-copy ambiguity。

可采用 modular/threshold counter为每个 exchangeability class保存高负载 residue，
并在高负载时让相应 pair永久 YES。这正回到 algebraic threshold quotient；若为
所有 pair预分配 counters，state数过大。若只为出现的 heavy classes动态分配，又要
维护 class dictionary，其 fingerprints/pairs 与 allocation routing必须计费。

因此 Theorem 2.1 消除了 orientation metadata，却没有消除 **class multiplicity
与 class allocation** 信息。

## 5. IBLT/reconciliation/peeling 路线审计

IBLT-like linear sketches有一个适合本问题的性质：insert/delete 对公开 hash cells
作可逆加减，不需要 insertion-time route；overloaded state未来删除后可重新变得
peelable。这与 threshold quotient 的“高负载时暂时放弃 query，保留恢复 residue”
机制相同。

但普通 IBLT cell为了识别 singleton通常保存 count、key XOR和checksum。对大
universe，key XOR携带 (Theta(\log|U|)) bits；即使换成 fingerprint，peeling出的
只是 fingerprint identity，collision会让错误 peeling潜在地产生 false negative。
为保持 one-sided、每 tape zero-FN，不能仅以高概率 checksum正确为由删除某个
cell contribution。

所以 reconciliation sketch 的优势是 route-free linear updates；其障碍是
one-sided safe decoding。当前没有一个已核实的 IBLT theorem直接给出本模型下
低于 (2.349083n) 的 fixed-state constant。

## 6. 多副本 route-free AND 也无收益

另一完全 route-free方案是让每个 key同时更新 (d) 个独立 threshold quotients，
query取 AND。删除对所有副本执行公开逆更新，语义完全正确。

对每个副本 local rejection为 (ho_q(\lambda))，总 FPR 是

\[
\varepsilon=(1-\rho_q(\lambda))^d.
\]

在 (arepsilon=1/2) 下优化 (q,d) 的 fixed-state OGF rate，(d=1,q=3)
仍为 (2.349083440193\ldots)；(d=2) 的最佳值已约为 (3.52026)。误差乘法收益
远不足以补偿状态复制。

## 7. 可验证的新结论与剩余目标

本轮最实质的新结论是 Theorem 2.1：

> fingerprint-dependent alternate buckets 使同 fingerprint copies形成可交换类，
> state-dependent cuckoo relocation无需 per-key orientation metadata即可支持合法
> key-only deletion。

这缩小了真正的信息账单。成功构造只需解决：

1. exchangeability-class multiplicity的 lossy reversible编码；
2. dynamically allocated heavy-class counters的 succinct dictionary；
3. fixed worst-case state下的 overflow-free fallback；
4. fallback产生的 accepted-union仍满足 pointwise FPR。

一个合理的新 upper-bound primitive应把 small classes存在 slots 中，heavy classes
切换为 threshold/ALL-YES counters，并证明所有 class allocation states可在
(<0.079n) metadata内编码，从而让 support-only two-choice benchmark
(2.12161n) 真正低于 (2.20061n)。目前没有完成该账本，因此不能宣称新 upper
bound。

## 8. 文献定位边界

已有动态 cuckoo/quotient filters、succinct dictionaries、IBLT和工程型
elastic/flexible filters都与上述机制相邻。这里没有完成新的在线文献优先权检索，
也不声称 exchangeable deletion 从未被工程实现使用。可严格声称的是本文对其
one-sided语义和信息账本的形式化，以及 fixed-state arbitrary-history障碍。

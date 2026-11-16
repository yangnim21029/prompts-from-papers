# 程式作業回饋：測試案例與自然語言提示

兩份 prompt 都接收題目和學生程式。第一份提供失敗測試的輸入與預期輸出；第二份針對一個錯誤給自然語言提示，並要求不要直接修改程式。可按需要選用其中一種回饋。

論文為 *A Classroom Study of LLM-Generated Feedback Intervention in Introductory Programming*。

作者：Heickal, Hasnain、Lan, Andrew。

研究機構：麻薩諸塞大學阿默斯特分校。首次提交：2026-06-07；本頁依據 arXiv:2606.08807v1。

## 研究怎麼做，結果如何

真實入門 Python 課程的 ProgFeed 資料涵蓋 215 名同意研究學生、17 個 lab、6,693 次提交。錯誤提交可獲 gpt-4o-mini 產生的自然語言提示、失敗測試案例，或只有固定測試的 pass/fail；模型看到題目敘述與學生程式。以學生－題目為單位估計 logistic regression 與 Cox hazard，標準誤按學生群聚。

自然語言提示相對無 AI feedback 與更高最終答對勝算相關：β=.84、OR≈2.33、p=.004；到達正確答案的 hazard ratio 為 1.09（p=.03）。失敗測試案例的最終答對關聯不顯著（β=.20，p=.40），HR=.92（p=.05），沒有穩定好處。OR 是勝算比，不能寫成答對機率增加 133%。

作者明確說明：feedback 只在失敗提交時觸發，曝露與答對狀況相依，所以即使分派有隨機程序，本文分析是關聯、不是因果。結果是作業完成與提交序列，沒有直接證明無 AI 獨立考試或長期技能提升。自然語言提示仍可能不正確；失敗測試的效益尤其依有效性而異。

## 公開材料與使用方式

下方保留作者公開的模板原文，輸入資料、變數與輸出格式依各段說明。

## 原始 prompt 與配套材料

### 1. 程式回饋：產生會失敗的測試案例

將原文 Problem: ... / Code: ... 換成題目敘述與學生程式，取得輸入與預期輸出。

需要提供：題目敘述 Problem；學生程式 Code。

用途：程式回饋。原文範圍：完整公開的 Group 1 提示；Problem: ... 與 Code: ... 中的省略號是待填入的題目與學生程式位置。

#### Prompt for Failing Test Case Feedback (Group 1)

```text
The student is given the problem and asked to implement the specified function(s). You can see their code below. Can you give a test case that would cause the student’s code to fail? Only give the test case with the expected output. Do not explain why it fails. Do not include any markdown formatting. If the test case involves a list, use explicit values rather than variable names.

Problem: ... Code: ...
```

原檔：`failing-test-case-feedback-excerpt.md`。來源定位：`S3.SS5.SSS0.Px1`。

### 2. 程式回饋：自然語言除錯提示

填入題目與錯誤程式，針對一個問題給提示；原文禁止直接修改程式或提供測試案例。

需要提供：題目敘述 Problem；學生程式 Code。

用途：程式回饋。原文範圍：完整公開的 Group 2 提示；Problem: ... 與 Code: ... 中的省略號是待填入的題目與學生程式位置。

#### Prompt for Natural Language Feedback (Group 2)

```text
The student is given the problem and asked to implement the specified function(s). You can see their code below. Can you give a brief natural language hint explaining why the code is failing? Refer to relevant parts of the problem description if appropriate. Do not suggest code changes. Do not give test cases. Focus on one important issue.

Problem: ... Code: ...
```

原檔：`natural-language-hint-excerpt.md`。來源定位：`S3.SS5.SSS0.Px2`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2606.08807v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

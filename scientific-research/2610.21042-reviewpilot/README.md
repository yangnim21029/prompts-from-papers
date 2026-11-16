# 系統性文獻回顧：篩選準則與資料擷取

ReviewPilot 把研究範圍、篩選準則、全文資料擷取和證據位置分開處理。附錄 G 公開完整模板，本頁整理各組模板的用途與所需輸入；原文需由頁末來源開啟。

論文為 *ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews*。

作者：Zhaoqian Xue、Shaoze Zhou、Xuexin Li、Junting Mu、Haozheng Liu、Zhongyin Wang、Yichun He、Renkai Ma、Hao Zhou、Sarah Bratt、Siyuan Ma、Chen Chen、Lingyao Li。

研究機構：亞利桑那大學、佛羅里達國際大學、Vanderbilt、UC Irvine、紐約大學、UIUC、Broad Institute of MIT and Harvard等。首次提交：2026-10-15；本頁依據 arXiv:2610.21042v1。

## 研究怎麼做，結果如何

多代理將研究問題轉成篩選準則與擷取schema，輸出理由、摘錄與來源位置。PERG的5,614筆標題摘要紀錄、178篇資料擷取論文；三種LLM；與專家標註比較。比較對象：同一模型的單一prompt方法及AgentSLR。

篩選macro F1最高0.776、擷取F1最高0.788；三個模型中，篩選F1高於AgentSLR 5.3–10.3個百分點、擷取F1高3.7–4.7個百分點。

比較的是AI工作流程；開發流程曾使用同一PERG資料池的評估分數，並非完全未見測試集；各設定僅跑一次；未直接量測人類節省時間。

## 公開材料與使用方式

論文附錄 G 公開了下列原文，但論文授權只允許 arXiv 散布，官方程式庫也未提供 LICENSE 或其他重刊許可。本頁提供 20 組模板、skills 與領域規則的用途及定位，全文請見頁末論文來源。

## 原文模板的用途與位置

### 1. Lead: project chat

依已確認狀態回答專案問題。

需要提供：專案狀態、對話歷史、當前問題。

原文定位：`A7.SS1.p2 through A7.SS1.p3`。

### 2. Lead: criteria chat

起草可觀察的納排準則變更。

需要提供：目前篩選準則、研究範圍、使用者修改要求。

原文定位：`A7.SS1.p4 through A7.SS1.p5`。

### 3. Lead: schema chat

起草擷取欄位變更。

需要提供：既有 schema、目前狀態、修改要求。

原文定位：`A7.SS1.p6 through A7.SS1.p7`。

### 4. Search: system + strategy skill

搜尋策略代理的系統規則與 skill。

需要提供：研究描述與檢索限制。

原文定位：`A7.SS2.p2`。

### 5. Search: initial strategy

產生初始檢索策略。

需要提供：專案聊天與檢索條件。

原文定位：`A7.SS2.p3`。

### 6. Search: strategy revision

修訂檢索策略。

需要提供：原策略及修訂意見。

原文定位：`A7.SS2.p4`。

### 7. Search / Prompt: rejected-response retry

依 schema／規則驗證錯誤重試。

需要提供：遭拒回應及驗證錯誤。

原文定位：`A7.SS2.p5`。

### 8. Prompt agent: system prompts + design skill

包含篩選指引與 schema 系統規則及共用 prompt-design skill。

需要提供：研究問題、篩選或擷取任務。

原文定位：`A7.SS3.p2 through A7.SS3.p4`。

### 9. Prompt agent: screening guidance draft + review

先產生篩選指引，再按原 checklist 審查草稿。

需要提供：研究範圍、納排條件、第一版草稿。

原文定位：`A7.SS3.p5 through A7.SS3.p6`。

### 10. Prompt agent: extraction schema

產生 JSON schema。

需要提供：欲擷取欄位與研究需求。

原文定位：`A7.SS3.p7`。

### 11. Prompt agent: coding rules draft + review

產生欄位編碼規則並檢查草稿。

需要提供：schema、領域規則、草稿。

原文定位：`A7.SS3.p8 through A7.SS3.p9`。

### 12. Screening: system + skill + per-record user

逐筆篩選並留下依據。

需要提供：標題、摘要、研究範圍、納排準則。

原文定位：`A7.SS4.p2 through A7.SS4.p3`。

### 13. Screening: PERG domain rules

保留原附錄的完整領域納排規則與不確定處理說明之來源。

需要提供：Lassa、Nipah、SARS、Zika 的研究範圍。

原文定位：`A7.SS4.SSS1`。

### 14. Extraction: system + skill + per-paper user

逐欄擷取、原文證據與來源位置。

需要提供：全文、schema、coding rules。

原文定位：`A7.SS5.p2 through A7.SS5.p3`。

### 15. Extraction: abstract-only fallback

全文不可得時先依摘要擷取，保留無法確定的欄位。

需要提供：沒有全文的論文標題與摘要、schema。

原文定位：`A7.SS5.p4 through A7.SS5.p5`。

### 16. Extraction: web fallback

依論文識別資訊查找尚未填入的欄位，回傳受來源支持的值。

需要提供：仍空缺的欄位、論文識別資訊、官方頁面與搜尋式。

原文定位：`A7.SS5.p6 through A7.SS5.p7`。

### 17. Extraction: PERG coding rules

保留原附錄的模型類型、隨機性、程式可用性、傳播方式與介入措施規則之來源。

需要提供：Ebola、SARS、Zika、Lassa 的論文與欄位。

原文定位：`A7.SS5.SSS1`。

### 18. Categorization: systems + skill

包括分類規劃、單類或多類歸屬的 system 及共用 skill。

需要提供：分類模式與既有證據。

原文定位：`A7.SS6.p2 through A7.SS6.p5`。

### 19. Categorization: category plan

建立定義明確的分類計畫。

需要提供：研究目標、已擷取資料、分類模式。

原文定位：`A7.SS6.p6 through A7.SS6.p7`。

### 20. Categorization: single / multiple assignment

將論文分到單一或所有受證據支持的類別。

需要提供：允許類別、定義、每篇證據。

原文定位：`A7.SS6.p8 through A7.SS6.p9`。

## 來源與授權

論文授權：arXiv non-exclusive distribution license。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[arXiv 論文](https://arxiv.org/html/2610.21042v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

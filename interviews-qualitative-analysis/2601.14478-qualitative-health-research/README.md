# 質性分析：整理據點摘要與跨訪談證據

作者公開四個程式檔，分別處理主題整理、跨據點綜整、檢索問答與去除重複證據。使用時需先由研究者準備照護面向、碼本與人工範例，再核對模型引用的原始訪談。

論文為 *Large Language Models for Large-Scale, Rigorous Qualitative Analysis in Applied Health Services Research*。

作者：Sasha Ronaghi、Emma-Louise Aveling、Maria Levis、Rachel L. Ross、Emily Alsentzer、Sara Singer, for the iPATH investigators。

研究機構：Stanford University（史丹佛大學）、Harvard University（哈佛大學）、Impactivo LLC。首次提交：2026-01-20；本頁依據 arXiv:2601.14478v1。

## 研究怎麼做，結果如何

研究涵蓋 12 家健康中心的 167 份訪談，約 133 萬個英文字。第一項工作以人工先寫好的據點摘要為輸入，整理 22 個照護實務面向；第二項工作由研究者定義 19 個編碼與 177 個子問題，結合檢索、摘要與引文核對。

團隊在九個月的介入設計期限內，把跨據點綜整與大規模訪談資料用於回饋及方案修訂。作者依三份訪談的人工分析計時外推，若全體材料都採同樣人工流程，約需 93 個工作週。這個估計沒有量測 AI 實際節省多少工時。

實務案例與工時外推，不是隨機對照的加速效果；仍需質性專家定義碼本、檢查引文與解釋；RAG與資料處理也是效果的一部分。

## 公開材料與使用方式

論文 PDF 依 CC BY 4.0 保存。官方程式庫沒有 LICENSE 或其他再散布聲明，本頁提供四個原始檔的固定版本來源。程式庫目前名稱為 LLMsforQualiattiveHealthServicesResearch。

## 原文模板的用途與位置

### 1. 將據點摘要按主題整理

整理原始摘要中的主題，保留來源文字，將剩餘內容放入其他類別，交由研究者檢查分類。

需要提供：各據點的人工摘要、照護面向與定義。

原文定位：`task1_organize_themes.py`。

### 2. 跨據點綜整與回饋

依指定面向整合跨據點資料，辨認可供實務回饋的差異與做法；人工範例也屬輸入的一部分。

需要提供：面向定義、各據點摘要、四份人工綜整範例。

原文定位：`task1_cross_site_synthesis.py`。

### 3. 以檢索片段回答質性研究子問題

用檢索取得的訪談片段作答並附引文，後續仍需把引文與原始逐字稿核對。

需要提供：訪談片段、碼本、子問題與來源識別。

原文定位：`task2_user_interface.py`。

### 4. 整併、去重與相關性排序

整合輸出、移除重複引文，再依相關性排序。檔案同時含程式處理與 LLM 模板，需配合資料欄位使用。

需要提供：各子問題的模型輸出與原始逐字稿。

原文定位：`task2_concatenate_deduplicate_sort.py`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2601.14478v1) · [官方程式固定版本](https://github.com/sronaghi/LLMsforQualiattiveHealthServicesResearch/tree/eb7cc37b16ea4e052b78903272e3a66fa4017cb1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

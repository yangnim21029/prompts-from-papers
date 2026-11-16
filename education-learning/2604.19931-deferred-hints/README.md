# 程式除錯提示：先自己判斷，再用 AI 協助

公開的 GPT-prompt.txt 要求模型依題目、正確程式和錯誤程式產生除錯提示。研究介入還包含學生先獨立分析、再取得 AI 協助的時間安排。此處提供原始檔的閱讀與下載來源。

論文為 *Hint-Writing with Deferred AI Assistance: Fostering Critical Engagement in Data Science Education*。

作者：Singh, Anjali、Brooks, Christopher、Li, Warren、Kim, Juho、Wang, Xu。

研究機構：密西根大學、德州大學奧斯汀分校、KAIST、Learning Data Insights。首次提交：2026-04-21；本頁依據 arXiv:2604.19931v1。

## 研究怎麼做，結果如何

97 名研究所學生參加課程內兩週隨機實驗，條件為 Baseline（獨立寫提示）、AI-assistance（按需看 GPT-4 提示）、Deferred AI-assistance（先獨立寫，再看 AI 並修訂）。以 rubric 評估學生提示品質與錯誤涵蓋，並記錄投入時間。97 人完成前測、62 人完成後測；知識測驗分析另以 propensity matching 形成 55 人。

混合效應模型中，Deferred 對 Baseline 的提示品質係數為 1.096（SE=.37，p=.003）；Tukey 校正的兩組比較 p=.01。辨識錯誤並排除多餘資訊的 Level 1 指標，Deferred 也高於 Baseline（p=.03）。55 人知識後測的組間差異不顯著（p=.18），不能把「寫出更好的提示」改寫成已證實「學得更多」。

實驗於 2023 年使用 GPT-4；學生後測流失、樣本偏小，第一週 deferred 條件花費更多時間，成效不能單純歸因於模型。AI 提示也可能把冗餘或不佳表述帶入學生答案。完整 GPT prompt 可在 OSF 讀取，但 OSF node 與 README 未授予再散布權；故此篇只公開合法 PDF 與來源連結。

## 公開材料與使用方式

已核對 OSF 的 GPT-prompt.txt 全文；OSF 專案與 README 未提供再散布授權，因此本頁保留用途、輸入與原始檔連結。論文 PDF 依 CC BY 4.0 保存。

## 原文模板的用途與位置

### 1. 資料科學除錯提示（GPT-prompt.txt；僅原始來源）

原始模板請由 source 連結讀取；它要求產生少於 100 字的提示，協助初學者找出錯誤而不直接揭露完整答案。本專案保留索引與使用說明，未重刊模板。

需要提供：作業問題敘述 <Programming Assignment Problem Statement>；正確程式 <Correct Code>；錯誤程式 <Inorrect Code>（原文拼字如此）。

原文定位：`OSF project w538q；GPT-prompt.txt；file GUID 9ubcy`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2604.19931v1) · [OSF 原始材料](https://osf.io/download/9ubcy/?view_only=352e55d06c5543c581b1885702dd4172) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

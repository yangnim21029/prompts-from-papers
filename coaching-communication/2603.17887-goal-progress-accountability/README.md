# 目標進展研究：目標與回饋的事後編碼

作者公開的三份模板用來評目標明確度、分類目標領域，以及編碼參與者回饋。實驗使用的 Leon 教練完整 prompt 尚未找到。下方說明的是研究測量工具，可從附錄 A5、A6、A8 閱讀原文。

論文為 *AI-Assisted Goal Setting Improves Goal Progress Through Social Accountability*。

作者：Michel Schimpf、Julian Voigt、Thomas Bohné。

研究機構：University of Cambridge、Technical University of Munich。首次提交：2026-03-18；本頁依據 arXiv:2603.17887v1。

## 研究怎麼做，結果如何

預註冊三組隨機試驗，517 位英美在職成人被分到無支援控制、結構化反思問卷或 Claude Sonnet 驅動的 Leon 聊天教練。最後主要分析包含 323 人（105／111／107），為全體隨機樣本的 62.5%；兩週自陳目標進展為主要結果。問卷要求至少作答 20 分鐘。公開 prompt 是事後目標編碼與質性回饋編碼。

AI 相較無支援控制，兩週進展平均 3.45 vs. 3.02（1–7 分），d=.33、p=.016。

AI 與結構化反思問卷的進展差異不顯著（d=.08、p=.540）；不能說 AI 已勝過優良的自我反思工具。

AI vs. 問卷的預註冊中介模型中，問責感間接效果 .15，95% CI [.04,.31]；self-concordance 中介不顯著。AI vs. 無支援對照則沒有顯著的問責感中介。

追蹤只有兩週且目標進展為自陳；樣本流失限制外推。

只有單一模型設定，沒有真人教練對照；英美在職、英語使用者不代表其他族群。

目標明確度、領域分類為探索性 LLM 編碼，需要人類驗證與預註冊複現。

AI 組許多目標超出職涯範圍，因此主要結果是個人所選目標的進展，不能嚴格視為純職涯績效。

## 公開材料與使用方式

三份公開模板都用於事後編碼。論文採 arXiv non-exclusive distribution license，未找到可供本庫重刊的授權；作者所列教練程式庫在查核時回傳 404。此頁只提供已確認的附錄來源。

## 原文模板的用途與位置

### 1. Goal specificity coding

對時間明確度與結果可量測性各評 0–2 分；用於事後分析，不是教練。

需要提供：GOAL TEXT；可選 CONTEXT；主分析使用 [no additional context]。

原文定位：`Appendix A5`。

### 2. Goal domain classification

將目標分類為 career／non-career；用於探索性分析。

需要提供：goal1、goal2、goal3。

原文定位：`Appendix A6`。

### 3. Qualitative feedback coding

編碼整體幫助程度、益處、挑戰與功能需求主題；用於研究回饋分析。

需要提供：feedback_helpful_t2 原文。

原文定位：`Appendix A8`。

## 來源與授權

論文授權：arXiv non-exclusive distribution license。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[arXiv 論文](https://arxiv.org/html/2603.17887v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

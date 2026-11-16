# 網路騷擾情境：產生支持回覆

這篇研究實際使用的 prompt 很短：提供年齡、性別與收到的留言，請模型建議如何回應。原文只有三個位置式填空欄位，下方完整保留。研究沒有比較長 prompt 與短 prompt。

論文為 *Empathy on Demand: How Empathic AI Can Scale Emotional Support for Verbal Harassment*。

作者：Anouk Bergner、Philipp Winder、Christian Hildebrand。

研究機構：University of Geneva（日內瓦大學）、University of St. Gallen（聖加侖大學）。首次提交：2026-06-04；本頁依據 arXiv:2606.05995v1。

## 研究怎麼做，結果如何

第一項研究收集 3,652 份支持回覆，來源包含四種語言模型、216 位心理健康專業人士及非專業人士。第二項研究另招募 431 人閱讀所選回覆，評估支持文字的主觀效果。模型使用相同情境及指示，並改變尋求支持者的年齡與性別。

Study 2 中，閱讀模型回覆者的被理解感平均為 5.43，專家回覆為 4.15，非專家回覆為 4.39；因應自我效能分別為 5.45、3.83、3.96。作者報告模型與兩種人類來源的比較均 p < .001。這是一次閱讀支持文字後的評估，不代表長期心理治療效果。

短期、情境化單次文字評分；不能解讀為AI治療優於心理專業照護；使用者主觀感受並非長期臨床改善。

## 公開材料與使用方式

原始程式來自 OSF notebook。本庫只擷取實際任務字串，並保存作者的授權聲明：code 為 MIT、data 為 CC BY 4.0。

## 原始 prompt 與配套材料

### 1. 回應網路騷擾情境

原程式依年齡、性別與留言填入模板，要求模型提出如何回應的文字。這份原始 prompt 本身很短；研究成效沒有測試加長提示詞。

需要提供：三個位置式 {} 依序填年齡、性別與遭遇的留言。

用途：支持回覆。原文範圍：全文。

```text
I am a {} year old {}. Today someone wrote '{}' on social media to me. Provide me with an answer of how to respond to this comment.
```

原檔：`prompts/01-support-response.en.txt`。來源定位：`01_dataGeneration_llm.ipynb，prompt_skeloton`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/abs/2606.05995v1) · [OSF 原始材料](https://osf.io/pxj4n?view_only=defc9f54efc04e5a811a58bae22a1b5c) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。

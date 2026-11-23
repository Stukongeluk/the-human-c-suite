# CHRO: AI CV screening rollout (NL, BE, DE)

**BOTTOM LINE**
Don't switch on auto-reject. Roll the module out as a ranking tool, with a trained recruiter confirming every rejection. That keeps most of the speed. The setup you described (bottom 70% rejected, nobody looking) is the kind of decision GDPR Article 22 restricts, and it needs works-council steps in all three countries before anything goes live. Confidence: High on the legal blockers, Medium on the time and cost numbers.

As you asked for it, the setup would reject about 2,800 people a month, roughly 33,600 a year, without anyone reading what they sent. In retail, a lot of them are also your customers.

**WHAT**
- **Rejecting with no human involved is the case the law has in mind.** GDPR Recital 71 gives "e-recruiting practices without any human intervention" as its example. The exceptions are narrow: the decision has to be *necessary*, and a cheap human alternative undercuts that. Even when an exception applies, every rejected applicant must be able to get a human to look again and to contest the decision. [Verified] ([GDPR Art. 22](https://gdpr-text.com/read/article-22/))
- **The human step is cheap.** If a recruiter confirms the 2,800 low-ranked rejections at 1–2 minutes each in a sorted queue, that's about 47–93 hours a month: 0.3–0.6 FTE, or roughly €20–47k a year. That is the whole gap between auto-reject and human-confirmed reject. You keep the ranking either way, and the ranking is where the time saving comes from. [Assumed: minutes per CV, 150 productive hours/FTE/month, €65–75k loaded recruiter cost]
- **"Bias-free" is a sales claim. If the model discriminates, the liability is yours, not the vendor's.** The Netherlands Institute for Human Rights says employers [can't shift responsibility for discriminatory recruitment algorithms onto the vendor](https://www.hrpraktijk.nl/hr-tech/datagedreven-hr/werkgever-zelf-verantwoordelijk-voor-discriminerende-algoritmes-bij-sollicitatie-4-aandachtspunten/). A 2024 University of Washington test found that AI CV ranking [preferred white-associated names 85% of the time](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/). Your applicant mix adds its own risks: German CVs often carry a photo and date of birth, and Belgian ones arrive in Dutch, French and German. Until you've tested the model on your own mix, nobody knows how it behaves. [Verified: sources; Assumed: your applicant mix]
- **A "GDPR-compliant" product doesn't make your use of it compliant.** You are the controller. That means you owe a DPIA, a privacy notice that explains the logic, and an explanation to any rejected applicant who asks. The EU Court of Justice requires that explanation to cover [the "procedure and principles actually applied"](https://curia.europa.eu/jcms/upload/docs/application/pdf/2025-02/cp250022en.pdf); handing over the algorithm isn't enough. If you can't explain the score, that's your problem, not the vendor's. [Verified: CJEU C-203/22; Likely: DPIA required under Art. 35(3)(a)]
- **Works councils come before go-live in all three countries, and the AI Act deadline is close.**
  - Netherlands: the works council (OR) has a [consent right over hiring-policy rules](https://www.rendement.nl/instemmingsrecht-artikel-27-wor/nieuws/instemmingsrecht-van-de-or-bij-personeelsbeleid.html) under Art. 27(1)(e) WOR. If you go ahead without consent, the OR can [have the decision treated as never taken](https://www.praxikon.com/nl/posts/or-instemmingsrecht-ai-op-de-werkvloer).
  - Germany: the works council (Betriebsrat) has co-determination rights under §87(1) no. 6 BetrVG and under [§95 incl. 2a for AI-built selection guidelines](https://www.gesetze-im-internet.de/betrvg/__95.html).
  - Belgium: you must inform and consult employee representatives under [CBA No. 39](https://www.osborneclarke.com/insights/what-should-employers-belgium-consider-when-using-ai-workplace).
  - EU AI Act: CV filtering is [high-risk under Annex III](https://artificialintelligenceact.eu/annex/3/), and since the AI Omnibus took effect the deployer duties [apply from 2 December 2027](https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act). The system you configure now is the one that has to meet them.

  [Verified]

**WHY THIS MATTERS**
Removing the human saves about half an FTE. In return you take on:
- GDPR exposure of up to €20M or 4% of global turnover [Likely: Art. 83(5)]
- German discrimination (AGG) claims of [up to three months' pay per rejected applicant, filed within two months of the rejection](https://www.gesetze-im-internet.de/agg/__15.html)
- a Dutch OR that can void the rollout
- thousands of customers a month getting a no from a machine

A fixed 70% cut is also the wrong lever. In a strong applicant pool it throws away people you would hire, and in a weak one it lets the wrong people through.

**HOW TO ACT**
1. **Keep auto-reject switched off.** Lock it at tenant level and allow scoring only in a sandbox. Owner: ATS owner + Head of TA. Deadline: Fri 27 Nov 2026.
2. **Get evidence from the vendor and test the model yourselves.**
   - Send the vendor the 16-question evidence request in the plan. Owner: Head of TA + DPO + Procurement. Deadline: send by Fri 4 Dec 2026; answers due Fri 8 Jan 2027.
   - Run a paired-CV audit on synthetic CVs in the sandbox: identical CVs that differ only in name, age, gender, career gap, photo or language. Owner: TA analytics. Deadline: Fri 22 Jan 2027.
3. **Complete the DPIA and update the applicant privacy notice.** Owner: DPO. Deadline: Fri 22 Jan 2027.
4. **Open the works-council tracks.**
   - NL: consent request to the OR.
   - DE: inform the Betriebsrat early under §90 and negotiate a works agreement (Betriebsvereinbarung).
   - BE: CBA No. 39 consultation.

   Owner: HR Directors NL/BE/DE + employment counsel. Deadline: first meetings by Fri 18 Dec 2026; agreements targeted by 31 Mar 2027. Germany may take longer.
5. **Run shadow mode for 8 weeks, then a gated pilot.** In shadow mode the AI scores every application while recruiters decide as they do today, without seeing the scores. After that comes an assisted pilot in one country and one job family. Owner: Head of TA. Deadline: go/no-go on 2 Apr 2027; pilot runs Apr–Jun 2027.

**RISKS**
- **Rubber-stamping.** If recruiters click "confirm" without reading, the score effectively becomes the decision, and you're back under Article 22. This is the logic of the CJEU's [SCHUFA](https://twobirds.com/en/insights/2023/global/key-takeaways-from-the-schufa-case-of-the-cjeu) ruling. Warning signs: an override rate near 0%, or under ~15 seconds per review. Countermeasure: a monthly blind second review of a sample.
- **Inherited bias.** If the vendor trained on your past hiring decisions, the model has learned your past bias. Ask directly, and if the answer is yes, require evidence that it has been corrected.
- **Silent model updates.** Vendor updates can change results without notice. Put version pinning and a re-test before every new version into the contract.
- **Germany runs late.** Don't run shadow mode there without a pilot agreement with the Betriebsrat.
- **The weakest point of this plan** is my 1–2 minute review estimate. Shadow mode will show the real figure.

**YOUR DECISION**
- **Option A: auto-reject the bottom 70%, no human (as asked).**
  - Upside: about 0.3–0.6 FTE more time saved than B.
  - Downside: in my read it isn't lawful as designed, it has no works-council basis, and the bias is untested.
- **Option B: the AI ranks and explains; a recruiter confirms every rejection in a batch queue.**
  - Top candidates are contacted within 2 working days.
  - Thresholds are set per job family from shadow-mode data instead of a fixed 70%.
  - Upside: most of the speed, it holds up under GDPR and the AI Act, and works councils can sign it.
- **Option C: B, plus auto-reject only on objective hard requirements the candidate declares, such as the right to work.**
  - The requirements are shown before anyone applies, and every rejection includes a link to request human review.
  - Only after DPIA and counsel sign-off.

**Recommendation:** start with B now and revisit C at the September 2027 review, once you have your own data.

**DETAIL:** `rollout-plan.md` (same folder) has the full plan: phases and gates, exit thresholds, the vendor questions ready to send, the paired-CV audit method, candidate notice text, the track for each country, monitoring and kill switch, the AI Act checklist, and who has to sign off.

Sign-off needed before go-live: your DPO and employment counsel in NL, BE and DE. This is people-strategy advice, not legal advice.

*Tags: [Verified] = checked against the law or a named source; [Likely] = reasonable reading, not checked against the source; [Assumed] = not checked against your data. There's no company context on file, so the staffing and cost figures are assumptions. The plan lists them.*

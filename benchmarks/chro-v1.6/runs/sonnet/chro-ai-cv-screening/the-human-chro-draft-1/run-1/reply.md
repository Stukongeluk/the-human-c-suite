I'd switch the module on, but not as an auto-reject. Let it score every CV and show recruiters why, and keep a person on every rejection. A pilot comes first, using your own past applications.

**Why not auto-reject the bottom 70%**
- **It is probably unlawful as designed.** Under GDPR Article 22, an automatic rejection that significantly affects someone is generally not allowed without a legal exception and safeguards. The CJEU (SCHUFA, C-634/21) also treats a score a recruiter simply follows as the decision itself. So "a recruiter could look" doesn't fix it.
- **It's high-risk under the EU AI Act.** CV screening is on the high-risk list. The deployer duties (human oversight, logs, monitoring, informing workers' representatives and candidates) apply from 2 December 2027 as currently scheduled. Build them in now.
- **The 70% is a quota, not a judgement.** It rejects the same share whether a pool is strong or weak, and no job requirement sets it. That is 2,800 candidates a month, about 33,600 a year, never read by a person.
- **"Bias-free" is a claim to test.** Amazon dropped a CV-scoring tool that downgraded CVs containing "women's". A US court let an age-discrimination claim over Workday's screening proceed as a nationwide collective action in 2025. Ask the vendor for its bias audit and test data, then run the tool on your own past applicants and compare selection rates by group.
- **You need consent first.** In the Netherlands, the works council has a consent right over recruitment rules and over systems that process personal data or can monitor performance (WOR art. 27(1)(e), (k) and (l)). In Germany, a works council has co-determination (sections 95 and 87(1) no. 6 BetrVG), so check which entities have one. I haven't verified the Belgian specifics. Your counsel should confirm them.

**What I'd do instead (full plan attached)**
1. **Weeks 1-3: define the problem.** What hurts: recruiter hours, slow replies, agency spend? My rough estimate is that 4,000 CVs at about two minutes each is around one full-time equivalent, so check the real numbers before assuming the module is the answer.
2. **Weeks 1-8: bring in the works councils and your data protection officer.** Do this with the real numbers, before configuring anything. Complete the data protection impact assessment and send one candidate notice in all languages.
3. **Weeks 4-12: shadow test.** Run the tool on past applications only. Compare rates by gender, age, part-time history, nationality and country, and add a blind recruiter sample. Agree stop criteria up front.
4. **Months 3-6: pilot.** Use two or three role families against a control group. The tool scores and gives reasons, and a recruiter confirms every rejection. Low-scored CVs get a short structured review plus a weekly random full read. Candidates are told and can ask for a person.
5. **Month 6-7: scale only where it worked.** That means saved time with no adverse impact and equal or better quality of hire. The quarterly bias review and the named owner stay.

You'd likely capture most of the time savings this way. Structured first-round questions, knockout questions for legal must-haves (work permit, availability) and scheduling automation also cut load without judging anyone.

**Assumptions:** recruiter time per CV and your current reject rate are estimates until the ATS data is pulled, and the vendor's model uses no emotion recognition or sensitive-trait inference. This isn't legal advice.

**Two questions that change the plan:** what is the real bottleneck (hours, response time or agency cost), and which German and Belgian entities have a works council?

What am I missing, and what would make this wrong?

The plan is saved as `rollout-plan.md` in the same folder.

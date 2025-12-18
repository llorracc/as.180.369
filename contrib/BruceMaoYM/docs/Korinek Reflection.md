# Korinek Reflection (with Comments on Student Response)

## Initial Thoughts

Using AI in economics research felt like double-sided sword. It enables faster and machine learning but at the same time in a way eliminates one's critical thinking skills.

---

## First Draft Without AI

The paper touched on lots of things and highlighted a wide range of benefits from using AI in economic research. As you write, you can use it to synthesize text from bullet points and edit paragraphs for improvements in grammar, style, and clarity, ensuring the overall writing maintains a proficient level. 

I think one thing i noticed that was different than other writings i have read was the rating system the writer proposed. Essentially, there are 3 categories, ○ (empty circle) is experimental capabilities requiring significant oversight; ◐ (half-full) means it is useful but needs careful oversight; then ● (full circle) means it is highly useful and reliable. 

There are many different LLMs in the market such as Claude, Chatgpt, Deepseek, Grok etc. Most writing and data manipulation tasks rate as highly useful (●), while mathematical derivations remain experimental (○).

---

## Second Draft with Claude AI

The paper by Anton Korinek touched on numerous topics and highlighted a wide range of benefits from using AI in economic research. As you write, you can use it to synthesize text from bullet points and edit paragraphs for improvements in grammar, style, and clarity, ensuring the overall writing maintains a proficient level. The author specifically notes that LLMs can help with tasks like generating catchy titles, creating tweets to promote papers, and even evaluating text for its stylistic shortcomings.

One thing I noticed that was different than other writings I have read was the practical rating system the writer proposed. Essentially, there are three categories: ○ (empty circle) for experimental capabilities requiring significant oversight; ◐ (half-full) for useful capabilities that need careful oversight; and ● (full circle) for highly useful and reliable features.

There are many different LLMs in the market such as Claude 2 (which notably has a 100,000 token context window for processing entire papers), ChatGPT with GPT-4, and open-source options like Meta's LlaMA 2. The paper provides specific examples using these tools, demonstrating that most writing and data manipulation tasks rate as highly useful (●), while mathematical derivations remain experimental (○). Interestingly, the author found that coding assistance falls somewhere in the middle (◐), citing evidence that GitHub Copilot increased programmer productivity by 56% despite still requiring human oversight.

---

## Third Draft with Claude AI

Anton Korinek's paper provides a systematic examination of generative AI's impact on economic research, though his optimism warrants scrutiny. While he demonstrates that LLMs can synthesize text from bullet points and edit for grammar, style, and clarity, his own experiments reveal concerning limitations. For instance, when he asked GPT-4 to simulate the Solow growth model, the system correctly generated the code but then hallucinated its interpretation, incorrectly claiming capital approached a steady state despite assuming positive population growth—a basic economic impossibility.

The paper's three-tier rating system (○ for experimental, ◐ for useful but requiring oversight, ● for highly reliable) provides valuable nuance often missing in AI discussions. However, even "highly useful" applications have caveats. When Korinek asked GPT-3.5 about the second welfare theorem, it confidently returned the definition of the first theorem instead, a fundamental error that could mislead students.

The empirical evidence presents a mixed picture. While Peng et al. (2023) found GitHub Copilot increased programmer productivity by 56%, and Noy and Zhang (2023) showed ChatGPT made writers 40% faster, Korinek's own testing revealed persistent issues. Mathematical derivations remain particularly problematic: when deriving CES demand functions, GPT-4 repeatedly made algebraic errors, forgetting terms even after corrections. His attempts to have Claude 2 assess Federal Reserve statements showed the model could identify general hawkish tones but missed subtle policy shifts that human experts readily caught.

Perhaps most tellingly, Korinek frames his long-term predictions as "speculative," acknowledging that while LLMs excel at micro-tasks, their path to replacing economic researchers remains uncertain. His comparison to chess—where computers evolved from weak competitors to complete dominance—may overlook economics' fundamentally different nature: understanding human behavior requires judgment that current AI, despite processing massive datasets, still lacks.

---

## Fourth Draft with Claude AI

After reading Korinek's paper, I found myself both excited and skeptical about AI's role in economic research. The paper does an excellent job cataloging what these tools can actually do right now, not just what they might do someday. What struck me most was how honest Korinek was about the failures. When he tried getting GPT-4 to simulate basic economic models, it would write perfect code but then completely misinterpret the results. In one case, it claimed capital was approaching steady state when the model clearly showed exponential growth. That's not a small mistake; any first-year grad student would catch that.

The productivity gains are real though. Researchers using GitHub Copilot coded 56% faster, and writers with ChatGPT improved their speed by 40%. For my own BNPL research, these tools have been invaluable for specific tasks. I've used Claude to quickly extract payment patterns from hundreds of consumer complaint narratives, something that would have taken weeks to code manually. GPT-4 helps me reformat messy transaction data from different BNPL providers into consistent formats for analysis. When writing up findings about consumer behavior patterns, I'll often dump my rough notes into ChatGPT to get a cleaner first draft, though I always have to fix its tendency to overstate conclusions.

But here's what Korinek's paper really gets right: these tools are best for what he calls "micro-tasks." Need to convert a bibliography from APA to Chicago style? Perfect. Want to brainstorm factors affecting BNPL adoption rates? Helpful starting point. Trying to build a theoretical model of BNPL market equilibrium with information asymmetries? You're basically on your own. The math capabilities just aren't there yet, and even when the AI gets the algebra right, it often misses the economic intuition entirely.

For BNPL research specifically, I see AI as a research assistant, not a collaborator. It can help me process qualitative data about consumer experiences, generate initial hypotheses about market dynamics, and clean up my writing. But understanding why consumers choose BNPL over credit cards, or predicting how regulatory changes will affect market structure? That still requires human judgment about human behavior, something Korinek acknowledges might be the last frontier for AI in economics.

---

## Final Draft with Cursor and Claude AI

Korinek's paper provides a systematic framework for understanding AI in economic research through six application areas—ideation, writing, coding, data analysis, and mathematical derivations. His rating system (○ experimental, ◐ useful with oversight, ● reliable) clarifies where AI succeeds. Most writing tasks earn ● ratings, while mathematical derivations remain ○—a distinction accurate in my BNPL research.

Korinek's honesty about failure modes proves most valuable. When he had GPT-4 simulate economic models, it generated correct code but misinterpreted results entirely. The model claimed capital approached steady state while showing exponential growth—a fundamental error any graduate student would catch. This gap between technical execution and economic reasoning appears consistently.

The productivity evidence remains compelling. Researchers code 56% faster with GitHub Copilot, and writers improve speed by 40% using ChatGPT. In my BNPL research, I've used Claude to extract payment patterns from consumer complaints—work requiring weeks to code manually. GPT-4 standardizes inconsistent transaction data across providers.

However, when I've asked Claude for linear regression ideas for analyzing BNPL adoption, the suggestions are disappointingly generic and impractical. It proposes elaborate specifications with interaction terms that don't match my data constraints. The model lacks understanding of measurement issues, missing variables, or selection bias problems in real datasets. These limitations echo Korinek's observation that AI excels at micro-tasks, not complex analytical work. Building theoretical models of BNPL market equilibrium or designing empirical strategies accounting for endogeneity requires economic intuition these systems cannot provide. For BNPL research, I treat AI as a research assistant, not a collaborator. Understanding consumer decision-making and predicting regulatory impacts still requires human judgment about behavior—the frontier where AI falls short, as Korinek acknowledges.

*Note: I used Cursor and Claude AI to revise all drafts. Throughout the conversations, I contributed my own perspective and personal anecdotes about my BNPL research, pushed back on suggestions that were too idealistic or AI-sounding, and made sure we kept critical thinking about AI limitations rather than just describing capabilities. The back-and-forth helped me articulate the practical challenges—like when Claude gives me generic regression specs that don't fit my data—in a way that felt authentic to my actual experience.*

---
## Reflections on Zoe's Approach and Interactive AI Techniques (11/03/2025 Updated)

What struck me about Zoe's approach was how it lines up with what Korinek says about working with AI. Instead of just summarizing the paper, she treated it like something to actually talk about, which is basically what Korinek recommends for LLMs. Don't use one-shot prompts, have a conversation. That's the whole point of Korinek's framework. AI isn't supposed to replace researchers. It's supposed to work with them.

Having AI ask you questions before it does anything, and through that process, it becomes like a personalized tutor. Korinek mentions this explicitly when he talks about using LLMs to explain concepts. He notes that "follow-up questions that go into further detail can be very useful and allow the user to obtain personalized tutoring." This sounds simple, but it actually changes how you think about AI. Instead of treating it like a tool that just follows orders, you're using it to help figure out what you're even trying to ask in the first place. When you're doing economics research, getting the question right is usually the hardest part. If AI can push you to be more specific about what you want to analyze, what data you actually have, and what you're trying to find, you're way less likely to get back generic garbage that doesn't help.

I've found this especially useful for BNPL work, and it's been particularly valuable because I'm simultaneously learning econometrics while doing the research. When I'm trying to design an empirical strategy or analyze market dynamics, if I let the AI ask me things like "What exactly are you trying to explain here?" or "What's the biggest constraint in your data?", I have to actually answer those questions. Which means I'm figuring out my assumptions before I even start running code.

Here's where it gets interesting. The AI doesn't just help with the BNPL questions. It ends up teaching me econometrics concepts in real time. I'll be working on a regression specification to analyze why some consumers default on BNPL payments, and the AI will ask something like "Are you worried about omitted variable bias here? Income might affect both BNPL usage and default rates." Then I realize I don't actually understand why omitted variable bias is bad, or how to test for it, so I ask the AI to explain it using my BNPL example. Suddenly I'm learning econometrics theory, but applied to my actual research question. The concepts stick because they're tied to something concrete I care about.

Or I'll be trying to include both merchant category fixed effects and store-level fixed effects in my model, and the AI will ask "Are these perfectly collinear? If every merchant category maps to a specific store type, you might have perfect multicollinearity." I have no idea what perfect multicollinearity even means, so we have a conversation about it. The AI explains using my actual data structure. Maybe some merchant categories only appear at certain types of stores, so the fixed effects are perfectly correlated. Then it helps me think through solutions. Maybe I should use one or the other, or maybe I need to rethink my classification scheme.

This same thing happened with instrumental variables, which Korinek actually uses as an example in his paper. I was trying to figure out whether BNPL usage causes changes in consumer spending patterns, but realized that spending patterns might also affect BNPL usage. That's a classic simultaneity problem. When I asked the AI about this, it gave me the standard explanation about instrumental variables being useful for addressing endogeneity, but that's exactly what Korinek warned about. The first response is usually generic. The real learning happened when I pushed back and asked follow-up questions. "Okay, but what would actually work as an instrument for BNPL usage in my data?" The AI started asking me questions. "What external factors affect BNPL availability but not spending directly? Maybe geographic variation in BNPL provider coverage? Or changes in state-level regulations?" Through that back-and-forth, I wasn't just learning what instrumental variables are. I was learning how to think about finding valid instruments in my specific research context.

The questions themselves end up being useful, not annoying. It's like having someone force you to think through your research design before you waste time going down the wrong path. But more than that, it's like having a tutor who's always ready to explain the econometric concepts you don't understand, right when you need them, in the context of the problem you're actually trying to solve. Korinek is right that this personalized tutoring aspect is one of the most valuable features of working with LLMs. You get help with both the technical execution and the underlying understanding simultaneously. And as he notes, "when employing LLMs in this way, follow-up questions that go into further detail can be very useful and allow the user to obtain personalized tutoring." That's exactly what happens. The generic first answer isn't enough, but the iterative questioning process is where the real learning occurs.

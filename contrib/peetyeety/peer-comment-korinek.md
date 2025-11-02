# Peer Comment on Bruce's Reflection on Korinek's AI Paper

## What I Appreciate About Bruce's Reflection

Bruce's reflection stands out for its intellectual honesty and practical grounding. Rather than offering generic enthusiasm about AI capabilities, he provides a nuanced assessment anchored in his actual BNPL research experience. Three aspects particularly resonate:

**First, the specificity of failure modes**: Bruce doesn't just say "AI has limitations"—he shows exactly where it fails. His example of Claude providing "generic regression specs that don't fit my data" captures a critical problem I've encountered in my film tax credit research. When I asked Claude about control state selection for my difference-in-differences analysis, it suggested standard economic controls without understanding that my parallel trends assumption requires matching on pre-treatment motion picture industry trajectories, not just GDP and unemployment. The model doesn't grasp the empirical identification strategy nuances that distinguish good from mediocre research.

**Second, the research assistant vs. collaborator distinction**: Bruce correctly positions AI as useful for micro-tasks (data extraction, code standardization) but inadequate for macro-thinking (theoretical modeling, empirical strategy design). This maps precisely onto my experience. Claude helped me structure my literature review and identify the "reclassification problem" in QCEW data more clearly, but when I need to think through whether ACS migration data actually solves that problem—or just introduces different measurement issues—I'm on my own. AI can't evaluate whether my dual-data validation strategy strengthens or complicates causal inference.

**Third, methodological transparency**: Bruce's disclosure about using Claude for drafting is refreshing. His note that he "pushed back on suggestions that were too idealistic or AI-sounding" acknowledges the iterative human judgment required to produce authentic academic work, not just technically correct prose.

## How I Can Leverage These Insights in My Research Process

Bruce's reflection helps me articulate a clearer AI usage framework for my film tax credit project:

### 1. Leverage AI for Data Infrastructure, Not Research Design

**Where AI helps**: Bruce's 56% coding speedup with Copilot aligns with my experience. I should use Claude/Copilot to:
- Write QCEW data download and cleaning scripts
- Generate synthetic control implementation code
- Create event study visualization code
- Standardize ACS occupation code mappings across years

**Where AI fails**: Bruce's generic regression spec problem warns me not to rely on AI for:
- Choosing control states for my DiD specification
- Deciding which economic controls to include (or exclude to avoid bad controls)
- Determining whether to cluster standard errors at state vs. state-year level
- Interpreting whether QCEW employment gains without ACS migration gains mean reclassification or measurement error

**Actionable takeaway**: I should create a "decision log" documenting which research choices came from AI suggestions vs. my own judgment vs. literature guidance. This forces me to own the analytical strategy rather than defaulting to AI recommendations.

### 2. Use AI for Literature Synthesis, But Not Literature Evaluation

**Where AI helps**: Claude effectively synthesized how Thom (2018), Rickman & Wang (2020), Bradbury (2020), and Owens & Rennhoff (2024) connect to form a narrative arc in my literature review. It identified the "persistent puzzle" framing and reordered papers for logical flow.

**Where AI fails**: When I asked Claude whether my ACS migration validation actually addresses Rickman & Wang's limitations, it gave an enthusiastic "yes" without critically examining whether:
- ACS migration data has sufficient sample size for motion picture occupations by state-year
- Residential moves lag employment changes (people might work in CA before officially moving)
- High-skill film workers might maintain multiple residences, defeating the migration proxy

Bruce's capital-steady-state misinterpretation example warns me: AI can execute technical tasks correctly while fundamentally misunderstanding the research question.

**Actionable takeaway**: I should explicitly ask skeptical questions: "What are three reasons my ACS migration strategy might NOT solve the reclassification problem?" This forces critical evaluation rather than confirmation bias.

### 3. Treat AI as Pre-Reviewer, Not Co-Author

Bruce's "research assistant not collaborator" distinction clarifies how I should position AI in my workflow:

**Pre-drafting phase**: Use AI to explore literature connections, identify data sources, debug code
**Drafting phase**: Use AI for prose clarity, section transitions, tightening arguments
**Critical phase**: Do NOT use AI to evaluate whether my findings are meaningful, whether alternative explanations exist, or whether my contribution matters

The most dangerous use of AI is asking "Is this research contribution significant?" because it will always say yes. Bruce recognizes this—his reflection demonstrates human judgment about where AI adds vs. subtracts value.

**Actionable takeaway**: I should reserve "big picture" questions for human advisors and peer reviewers. AI can help me articulate my argument more clearly, but it cannot tell me whether the argument is worth making.

## The Meta-Lesson: Korinek's Framework Requires Discipline

Bruce's reflection demonstrates what Korinek's framework demands: researchers must develop judgment about where the ○/◐/● ratings apply to their specific research. "Writing" might be ● in general, but "writing a compelling research contribution narrative" remains ○. "Coding" might be ◐, but "choosing the right empirical specification" remains firmly in human territory.

For my film tax credit research, this means:
- Use AI extensively for QCEW/ACS data wrangling (◐)
- Use AI moderately for literature review synthesis (◐)
- Use AI minimally for research design decisions (○)
- Keep AI away from interpreting whether my findings matter (○)

Bruce's honesty about his BNPL research experience—where Claude fails at regression design despite succeeding at data extraction—provides the template I need: specific, grounded, and appropriately skeptical about AI's role in serious empirical research.


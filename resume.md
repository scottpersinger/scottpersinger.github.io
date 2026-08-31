# Scott Persinger

San Francisco, CA
[scottpersinger@gmail.com](mailto:scottpersinger@gmail.com)
[scottpersinger.com](https://scottpersinger.com) / [X](https://x.com/persingerscott) / [GitHub](https://github.com/scottpersinger) / [LinkedIn](https://www.linkedin.com/in/scottpersinger) / 510-708-4560

## Summary

Hands-on product and engineering team leader. I thrive on building new teams, products, and companies that leverage leading edge technology. I've built and shipped multiple products into large enterprises with high security and compliance demands. I look for high growth opportunities that leverage my ability to synthesize product vision, technical leadership, and the ability to ship every day.

I have experience leading teams of 5–100. I've worked across domains in fintech, ad tech, travel, consumer mobile, B2B SaaS and cloud infrastructure.

## Experience Highlights

- Co-founder & CTO of BizTrip AI, backed by Andrew Ng. Building an Agentic AI product for corporate travel, based on user personalization but integrated with the traditional travel tech stack through Sabre.
- Drove enterprise readiness at BizTrip AI: SOC 2 Type I (Type II in progress) and PCI DSS compliance, plus a production AI deployment at Moderna, a regulated pharmaceutical enterprise.
- Founder of [Supercog.ai](https://supercog.ai), an early pioneer in agentic systems and agent dev tools.
- SVP, Engineering, [Tatari Inc](https://www.tatari.tv). Grew the org from 20–100. Built a world-class engineering team to build the Tatari advertising and analytics platform.
- Grew the Alternative Payments business at Stripe by 3X. Expanded engineering group from 4 to 28 across four locations (SF, Seattle, Dublin, Singapore).
- Senior Director, Heroku. Led the Heroku platform group (50 people), reporting to the VP Engineering. Helped Heroku achieve PCI and HIPAA compliance.
- Co-founded Cloudconnect.com with Adam Gross. Principal engineer for the Cloudconnect product. Company acquired by Salesforce (integrated into the Heroku subdivision) in 2013. Grew the Heroku Connect team and business to $10m ARR.
- Hired and mentored students and new grads from: Waterloo, Western University, UC Berkeley, UCI, UCLA, Syracuse

## Education

Computer Science, University of California at Berkeley

## Employment History

### 2025 – Present, BizTrip AI

*Co-founder & CTO*

Co-founded BizTrip AI, an AI-powered corporate travel planning platform. The company was co-founded with Tom Romary and with backing from AI Fund - operated by Andrew Ng. Andrew Ng is listed as a co-founder and invested personally in the company. BAG VC and RRE Ventures also invested.

I built the majority of the product, plus hired and managed a small, expert team. Shipped our initial AI booking tool in 4 months with a team of 3, deployed into production at Moderna (regulated pharma enterprise). Expanding from pilot to org-wide rollout across all ~1,000 US employees, including automated HR sync (SFTP) and downstream integration with the customer's existing TMC (Cain Travel).

I lead our "co-founder technical sales" efforts including social marketing, technical selling with the Head of Procurement or VP of Travel, pilot definition, scoping, and management.

My product responsibilities:

- Led SOC 2 Type I (Type II in progress) and PCI DSS compliance to meet the security bar for regulated enterprise customers including Moderna (pharma).
- Designed and built the Agentic travel planner (uses OpenAI and Anthropic models)
- Online reflection and memory system which allows the travel planner to automatically learn user preferences and improve recommendations over time
- Skills/MCP backend allows us to integrate new data sources (car rentals, on-time performance data, price prediction) and capabilities into the agent.
- Managed Sabre Corp. business and technical partnership.
- Enterprise readiness / platform: Led enterprise security and compliance: SOC 2 Type I completed (Type II underway) and PCI DSS in progress, including card vaulting for PCI-compliant booking flows. Built SSO support via Okta, plus audit logging and security event logging

Besides the product, I have evolved the team and software process as coding agents have radically transformed software creation:

**Retooled our development process around cloud agents.** Coached the team through the Copilot > Cursor > Claude Code transitions, then moved past the "IDE assistant" model entirely: much of our development now runs through cloud-hosted coding agents that team members dispatch and supervise rather than pair with. Deployed Slack-accessible coding agents so devs and PMs can kick off fixes, investigations, and prototypes from anywhere and stay unblocked under high velocity. Standardized the agent toolkit across the team — shared Skills and custom-built MCP connectors (including our Sabre integration) — so every agent session starts with full product context. Kept the process disciplined: AI-native development that avoids "tokenmaxing" and holds token costs under $300/month per team member.

**Upleveled the team into a single "product engineer" shape.** Rebuilt our roles and processes around the "product engineer", collapsing the traditional developer/PM split. With agents handling much of the code production, every team member — engineer or PM by background — is expected to own a product surface end to end: understand the customer problem, drive delivery, and drive adoption. Daily "Demo Time" keeps the whole team reviewing working product rather than status updates. The result: a team of this size ships ~20 PRs per day, and the AI-powered process has doubled our velocity from year 1.

**Built evals and agentic loops that automate development and improvement of the product itself.** Created the "agent trace" evals system that tests for correct agent behavior over long, complex planning sessions, giving us a regression gate for changes to the travel planner. Built an automated learning loop that analyzes live planning traces, drafts candidate improvements to the agent's instructions and behavior, and tests them against the evals before rollout. Deployed agentic loops for bug report investigation and planning session analysis, so triage and product-quality analysis run continuously instead of consuming engineer time. Together with the online reflection/memory system, this closes the loop: the product learns from production usage, and the development process improves the product with progressively less human effort.

### 2024 – Present, Supercog AI

*Advisor*

Founded this AI startup in Feb 2024 to build and explore agent systems. Operated primarily as a research lab as we evolved the technology and explored potential applications.

I left daily involvement to build Biztrip AI. The current team is focused on building a services business around enterprise agent adoption.

- Built **[Agentic](https://github.com/supercog-ai/agentic)**, our open-source agent framework, which preceded the frameworks from OpenAI, Anthropic, and Google. Our event driven design is still superior to many of the existing frameworks (although Langchain and Google did catch up and exceed what we built). Key elements of the design:
  - A deliberately thin agent loop calling LLM APIs directly, with multi-model support (OpenAI, Anthropic, and others via LiteLLM) and an actor-model runtime built on Ray.
  - A rich event system for background execution and notifications, human-in-the-loop waits (including indefinite pauses and webhook resumption), automatic context/token management, and dynamic tool addition and removal at runtime.
  - Support for multi-agent teams, RAG, and tools drawn from MCP, LangChain, and Composio, plus a production-tested tool library extracted from our commercial product.
  - Built-in logging and tracing of agent threads, tool calls, and LLM completions with token usage and timing telemetry.
- Co-designed an open **[agent protocol](https://github.com/supercog-ai/agent-protocol)** for cooperation between agents built on different tech stacks (LangGraph, SmolAgents, etc.). Rather than the "agents as tools" function-call model, the protocol treats agents as actors exchanging asynchronous event streams (Agent → Thread → Run → Events) over a REST/SSE transport, so long-running agents from different frameworks compose cleanly.
- Launched the self-service **Supercog agent builder** in Fall 2024 — similar products were launched by the AI labs months later. A web dashboard (SaaS at app.supercog.ai, plus a Docker-based local developer edition and on-prem installer) where users create agents with natural-language instructions, chat with them, and attach tools dynamically — including a "Tool Builder" agent that creates new capabilities on the fly.
- Shipped a portfolio of working agents and connectors on the platform: Deep Research, a browser-automating "Agent Operator", an automated daily Podcast Producer, a Meeting Notetaker, and a Morning News Reporter (text-to-speech); connectors for GitHub, email (AWS SES), web search, screenshots, image recognition, REST APIs, data visualization, and text-to-SQL querying over enterprise data.

### 2019 – 2024, Tatari Inc.

*SVP, Engineering*

Tatari builds the infrastructure to power TV advertising in the digital era. We use big data, advanced analytics and machine learning to automate linear and CTV campaign execution and optimization for hundreds of companies.

Grew the engineering org from 18 ("startup team") to over 100. I oversaw all budget (headcount and infrastructure) and delivery for the engineering group, including all product and platform engineering teams, SRE, Security and Support. I collaborated with the CEO and heads of Product, Sales, and Marketing to define and deliver on our technical and product strategy.

Primary accomplishments:

- Helped the company grow revenue by 5x (2019–2024).
- Recruited and developed line manager and manager-of-manager leadership levels, including 4 Directors and 8 line managers. Performed regular 1:1s and frequent skip levels.
- Hired and managed the early Product team, then helped to recruit the current VP of Product. Developed an effective matrix between Product and Eng.
- Defined IC and Manager job levels and expectations.
- Developed growth and promotion plans for my direct reports as well as Senior and Staff engineers, with promotions tied to levels structure.
- Hired and organized effective specialist teams within engineering around SRE, data engineering, ML, security, and support.
- Created career ladders for engineering ICs and managers. Created and refined the performance management processes.
- Fostered a high-bar, high velocity, *product delivery*-focused engineering culture by refining processes for hiring, promotion, planning, delivery, and support.
- Invested in a metrics-driven management culture (measuring velocity, health, quality and costs) to effectively scale the organization.
- Recruited and grew the *data engineering* group. Sponsored and guided multiple platform migrations to accommodate the explosion of data scale and metrics complexity in the product.
- Recruited the ML engineering team who collaborate with Data Science to build predictive analytics and automated bidding features for our platform.

### 2017 – 2019, Stripe

*Manager - APMs*

Built a new group at Stripe to extend pay-in services beyond credit cards to all other global payment methods ("alternative" payment methods including ACH, CA ETF, BECS debits, SEPA payments, Alipay and WeChat Pay plus many others).

- Built and scaled global pay-in and billing infrastructure processing payments across 15+ methods and multiple regions.
- Held both EM and PM responsibilities for most of my tenure.
- Hired new ICs in SF and Seattle (plus Seattle manager) plus international APM engineering teams in Dublin and Singapore.
- Developed the APM product roadmap with input from stakeholders on the Billing team, plus EMEA, APAC and Large User sales teams.
- Collaborated with Product UX, Risk, Merchant Intelligence, and Treasury teams to integrate new payment method flows into their respective areas.
- Launched bank transfer payments in the USA, UK, and Japan, navigating regional regulatory and data-residency requirements for each market.
- Launched support for WeChat Pay and Alipay
- Managed partnership and launch of BNPL payments with Klarna
- Worked closely with our internal architecture group to improve Stripe's internal payments architecture to allow globally distributed teams to build local payment method support.
- Defined program to measure and surface business and operational metrics across the APM portfolio.

### 2013 – 2017, Salesforce (Heroku)

*Senior Director - Platform Services*

Reporting to the VP Engineering, managed the 50 person platform services group including teams responsible for the primary user facing Heroku components (Dashboard and CLI), the Heroku Add-ons ecosystem and public API, Heroku CI, Heroku Metrics, the Heroku API, the app build pipeline, and the core Heroku control plane. During my tenure I emphasized a program to automate collection and reporting of our operational metrics. I also led the group responsible for evolving our microservices architecture.

*Manager - Core Services (2016)*

Owners of the Heroku platform API, internal API gateway, and event bus streaming service. This team focuses on improving the operational characteristics of the Heroku platform while collaborating extensively with numerous project teams looking to advance innovation on the platform. I doubled the team size and invested heavily in more support for microservice architectures.

*Manager - Connect Team (2014, 2015)*

Hired and managed the Connect team at Heroku, developers of the Heroku Connect product which provides bi-directional data-synchronization between Salesforce and apps on Heroku. Grew the Heroku Connect product from single digit to hundreds of customers and over $10m annual revenue. The Heroku Connect product was originated at Cloudconnect before its acquisition by Salesforce.

### 2012 – 2013, Cloudconnect.com (acquired by Salesforce)

*Co-founder*

Hosted web service for customer data synchronization and marketing automation. Architect and development lead for the Cloudconnect product.

Cloudconnect was in the inaugural class at the Heavybit incubator started by James Lindenbaum. The company was acquired by Salesforce.com (Heroku subsidiary) in November, 2013. The Cloudconnect product was relaunched as Heroku Connect.

### 2006 – 2011, Remixation, Inc. (acquired by Vevo)

*Co-founder*

**Showyou**

Lead developer of Showyou ([showyou.com](http://showyou.com)), the leading social video application for iPad and iPhone. Launched in April 2010, Showyou achieved immediate press recognition and saw 100k downloads in three months. The Showyou backend system analyzed video metadata for over 250k videos per day.

Worked with the CEO and design lead to design the product, then led the engineering team on implementation. Overall responsibility for application architecture including backend utilizing the Riak data store, 3rd party feed scanner using Node.js, and iOS and web client applications. Implemented the 2-dimensional panning video grid using Core Graphics which provides the core application experience. Managed Apple App Store submission and approval process.

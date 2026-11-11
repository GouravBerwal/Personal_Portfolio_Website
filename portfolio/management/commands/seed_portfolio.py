from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience


class Command(BaseCommand):
    help = "Seeds initial portfolio data for Gourav Berwal"

    def handle(self, *args, **options):
        self.stdout.write("Seeding portfolio data...")

        # 1. Profile
        Profile.objects.all().delete()
        Profile.objects.create(
            name="Gourav Berwal",
            title="Undergraduate Student @ CSE Dept., CGC University Mohali",
            sub_title="CGC University Mohali — Computer Science & Engineering",
            bio_1="I'm a Computer Science and Engineering student at CGC University, Mohali, with a strong interest in software development, data analytics, and building technology that solves real-world problems.",
            bio_2="I enjoy understanding how things work, exploring data, writing code, and transforming complex problems into simple, practical solutions. My approach combines analytical thinking with a passion for continuous learning and building.",
            bio_3="My technical interests include Python, SQL, Data Analytics, Data Visualization, and Backend Development. I enjoy working with data, identifying meaningful patterns, developing applications, and creating solutions that are both useful and scalable.",
            bio_4="Currently, I'm gaining professional experience as a Python Developer Intern at AlphaWizz, where I'm strengthening my development skills and learning how software is designed and built in a professional environment.",
            bio_5="Beyond technology, I believe in curiosity, consistency, and lifelong learning. I enjoy reading novels, listening to music, and exploring new ideas that challenge the way I think.",
            about_quote="I don't just want to write code. I want to build things that make a difference.",
            email="gouravberwal003@gmail.com",
            phone="+91 9516637166",
            resume_link="/resume/",
            nav_resume_link="/resume/",
            hero_avatar="images/Gourav.jpg",
            about_photo="images/Gaurav.jpg",
            hero_bg="images/CGC.jpg",
            contact_bg="images/World Map.jpg",
            instagram_url="https://www.instagram.com/_gouravgurjar__",
            linkedin_url="https://www.linkedin.com/in/gouravberwal/",
            github_url="https://github.com/GouravBerwal",
            leetcode_url="https://leetcode.com/",
        )
        self.stdout.write("  ✓ Profile seeded")

        # 2. Skills
        Skill.objects.all().delete()
        skills_data = [
            ("Python", "images/Python.png", "languages", 1),
            ("Django", "images/Django.svg", "languages", 2),
            ("Django REST API", "images/Django-API.svg", "languages", 3),
            ("MySQL", "images/MySQL.png", "db", 4),
            ("Git", "images/Git.svg", "tools", 5),
            ("GitHub", "images/GitHub.svg", "tools", 6),
            ("Google Cloud", "images/Google-Cloud.svg", "tools", 7),
            ("Excel / Sheets", "images/Excel.png", "data_bi", 8),
            ("Pandas", "images/Pandas.png", "data_bi", 9),
            ("NumPy", "images/NumPy.png", "data_bi", 10),
            ("Matplotlib", "images/Matplotlib.png", "data_bi", 11),
            ("Seaborn", "images/Seaborn.png", "data_bi", 12),
            ("Scikit-Learn", "images/scikit-learn.png", "data_bi", 13),
            ("Power BI", "images/power-bi-icon.png", "data_bi", 14),
            ("Tableau", "images/Tableau.png", "data_bi", 15),
            ("HTML", "images/HTML5.png", "web", 16),
            ("CSS", "images/CSS3.png", "web", 17),
            ("JavaScript", "images/JavaScript.png", "web", 18),
        ]
        for name, icon, cat, order in skills_data:
            Skill.objects.create(name=name, icon_image=icon, category=cat, order=order)
        self.stdout.write(f"  ✓ {len(skills_data)} Skills seeded")

        # 3. Projects (12 Premier Projects with Apple/MAANG Level Engineering Details)
        Project.objects.all().delete()
        projects_data = [
            {
                "title": "🏢 KirayaSaathi – Smart Rental & Property Management SaaS",
                "category": "filter-se",
                "tech_stack": "Python | Django | REST APIs | PostgreSQL | JavaScript | PDF Engine",
                "bullet_1": "Architected an enterprise-grade multi-tenant property management SaaS platform automating tenant onboarding, digital lease agreements, and automated PDF rent invoice generation for 100+ properties.",
                "bullet_2": "Engineered an algorithmic utility & electricity sub-meter calculation engine with auto-rollover billing logic, ledger balancing, and automated payment reconciliation workflows.",
                "bullet_3": "Constructed an executive real-time operational dashboard delivering live occupancy metrics, ARR forecasting, and automated overdue dues escalation with sub-second API latencies.",
                "image": "images/KirayaSaathi.png",
                "github_url": "https://github.com/GouravBerwal/KirayaSaathi",
                "order": 1,
            },
            {
                "title": "🏡 KiraayaGrid – Accommodation Discovery & Property Marketplace",
                "category": "filter-se",
                "tech_stack": "Python | Django | PostgreSQL | Full-Text Search | JavaScript | HTML5",
                "bullet_1": "Engineered a high-throughput, zero-brokerage accommodation marketplace connecting tenants with verified long-stay properties across major metropolitan hubs.",
                "bullet_2": "Implemented multi-parameter geo-filtering algorithms (location, budget brackets, room archetypes) with indexed B-Tree database queries, slashing search query latency by 45%.",
                "bullet_3": "Designed end-to-end property listing pipelines featuring automated client-side image compression, landlord identity verification, and direct tenant inquiry triage.",
                "image": "images/KirayaGrid.png",
                "github_url": "https://github.com/GouravBerwal/KirayaGrid",
                "order": 2,
            },
            {
                "title": "🩺 Digital Physiotherapy & Neurorehabilitation Telehealth Platform",
                "category": "filter-se",
                "tech_stack": "Python | Django | REST APIs | Google Meet Integration | PostgreSQL | JavaScript",
                "bullet_1": "Architected a secure digital telehealth consultation and neurorehabilitation scheduling engine with dynamic tier-based consultation packages and real-time slot booking.",
                "bullet_2": "Integrated automated video consultation link dispatch via Google Meet & Calendar APIs with dynamic clinical intake questionnaires for streamlined patient onboarding.",
                "bullet_3": "Engineered role-based clinician dashboard for monitoring patient recovery milestones, managing digital exercise prescription roadmaps, and processing payment webhooks.",
                "image": "images/NeuroRehab_Platform.png",
                "github_url": "https://github.com/GouravBerwal/Physio-NeuroRehab-Platform",
                "order": 3,
            },
            {
                "title": "🚨 AI-Powered Safety Analytics & Risk Prediction System (CSAPR)",
                "category": "filter-ml",
                "tech_stack": "Machine Learning | Python (Pandas, NumPy, Scikit-learn) | Predictive Modeling | Telemetry",
                "bullet_1": "Engineered an end-to-end predictive machine learning pipeline analyzing multi-dimensional incident patterns to forecast high-risk safety hazards with 89% classification accuracy.",
                "bullet_2": "Executed rigorous feature engineering, correlation analysis, and hyperparameter optimization across ensemble gradient-boosted models to isolate key incident contributors.",
                "bullet_3": "Designed modular, decoupled data ingestion pipelines built for scaling to live IoT telemetry streams, delivering real-time hazard alerts to proactive safety response teams.",
                "image": "images/CSAPR.png",
                "github_url": "https://github.com/GouravBerwal/CSAPR-Safety-Analytics",
                "order": 4,
            },
            {
                "title": "📊 Customer Behavior Analytics & Sales Insights Dashboard",
                "category": "filter-da",
                "tech_stack": "SQL (MySQL) | Python (Pandas, NumPy) | Power BI | Data Modeling",
                "bullet_1": "Developed an end-to-end data analytics and business intelligence pipeline modeling 100K+ retail transactions to identify key revenue drivers, churn indicators, and seasonal trends.",
                "bullet_2": "Optimized high-concurrency SQL queries with indexing and Common Table Expressions (CTEs), accelerating analytical report refresh cycles by 40% across multi-channel retail segments.",
                "bullet_3": "Constructed interactive Power BI executive dashboards surfacing customer lifetime value (CLV), purchase frequency, and seasonal product affinity metrics.",
                "image": "images/Customer.png",
                "github_url": "https://github.com/GouravBerwal/Customer-Behavior-Analytics",
                "order": 5,
            },
            {
                "title": "♻️ KachraWala – Smart Civic Waste Management System",
                "category": "filter-da",
                "tech_stack": "MySQL | Python | REST APIs | Spatial Clustering | JavaScript | System Design",
                "bullet_1": "Engineered a civic-tech logistics platform optimizing municipal waste collection workflows by analyzing spatial complaint clusters and identifying high-frequency waste zones.",
                "bullet_2": "Implemented normalized database architecture (MySQL) and automated spatial dispatch algorithms, reducing average public grievance resolution time by 32%.",
                "bullet_3": "Formulated predictive waste accumulation metrics to support dynamic fleet route optimization and municipal resource allocation.",
                "image": "images/Kachrawala.png",
                "github_url": "https://github.com/GouravBerwal/KachraWala",
                "order": 6,
            },
            {
                "title": "🛒 Amazon E-Commerce Architecture & Responsive UI",
                "category": "filter-se",
                "tech_stack": "HTML5 | CSS3 | JavaScript | Responsive Grid Architecture | DOM Manipulation",
                "bullet_1": "Built a production-grade, pixel-perfect e-commerce frontend architecture replicating core Amazon workflows (catalog browsing, dynamic cart, responsive navigation).",
                "bullet_2": "Engineered modular, reusable UI components leveraging CSS Flexbox and Grid, eliminating Cumulative Layout Shift (CLS) across mobile, tablet, and ultra-wide screens.",
                "bullet_3": "Optimized client-side asset loading and rendering performance, achieving high Lighthouse scores and sub-second First Contentful Paint (FCP).",
                "image": "images/Amazon.png",
                "github_url": "https://github.com/GouravBerwal/Amazon-Clone",
                "order": 7,
            },
            {
                "title": "🎬 Netflix Streaming Experience & Media UI",
                "category": "filter-se",
                "tech_stack": "HTML5 | CSS3 | JavaScript | CSS Animations | Media Queries",
                "bullet_1": "Developed a cinema-grade streaming interface clone with fluid horizontal carousels, responsive hero video banners, and dynamic movie title cards.",
                "bullet_2": "Implemented hardware-accelerated CSS transforms and smooth opacity transitions, delivering a 60fps native-app-like user browsing experience.",
                "bullet_3": "Built comprehensive device-adaptive layout systems, ensuring flawless typography and visual hierarchy scaling across all viewport dimensions.",
                "image": "images/Netflix.png",
                "github_url": "https://github.com/GouravBerwal/Netflix-Clone",
                "order": 8,
            },
            {
                "title": "📍 Smart In-Store Product Locator (Walmart Hackathon)",
                "category": "filter-se",
                "tech_stack": "Python | JavaScript | HTML5 | CSS3 | Search Optimization | Algorithm Design",
                "bullet_1": "Developed an algorithmic in-store routing prototype for Walmart Hackathon, enabling shoppers to locate items in real-time across large supermarket floorplans.",
                "bullet_2": "Engineered fast search and indexing algorithms with autocomplete querying, reducing in-store navigation friction and search retrieval latency.",
                "bullet_3": "Designed an intuitive, lightweight mobile-first interface optimized for weak network environments inside massive retail warehouse layouts.",
                "image": "images/Walmart.png",
                "github_url": "https://github.com/GouravBerwal/Walmart-Store-Locator",
                "order": 9,
            },
            {
                "title": "🌍 Hyperlocal Community Assistance Platform (NHN)",
                "category": "filter-se",
                "tech_stack": "Python | Django | REST APIs | JavaScript | HTML5 | CSS3",
                "bullet_1": "Engineered a neighborhood mutual-aid platform connecting community volunteers with localized emergency requests in real-time.",
                "bullet_2": "Designed low-friction request creation workflows and automated status notifications, improving volunteer response turnaround times by 35%.",
                "bullet_3": "Built modular REST-ready API architecture with decoupled data layers, enabling scalable integration with third-party geolocation and notification services.",
                "image": "images/NHN.png",
                "github_url": "https://github.com/GouravBerwal/Neighbourhood-Help-Network",
                "order": 10,
            },
            {
                "title": "🧠 Strategic Game Engine – Tic Tac Toe",
                "category": "filter-se",
                "tech_stack": "JavaScript (ES6+) | HTML5 | CSS3 | State Machine Architecture",
                "bullet_1": "Built an interactive state-driven game engine implementing Minimax-inspired evaluation logic for all 8 terminal board win-conditions.",
                "bullet_2": "Architected deterministic game state management with move validation, dynamic turn toggling, and undo/redo board history tracking.",
                "bullet_3": "Engineered clean event-driven DOM rendering with instant visual win indicators, zero dependencies, and 100% test coverage.",
                "image": "images/Tic Tac Toe.png",
                "github_url": "https://github.com/GouravBerwal/Tic-Tac-Toe-Game",
                "order": 11,
            },
            {
                "title": "🎮 Interactive Game Engine – Rock Paper Scissors",
                "category": "filter-se",
                "tech_stack": "JavaScript (ES6+) | HTML5 | CSS3 | Game State Logic",
                "bullet_1": "Engineered an interactive gaming engine with randomized computer decision logic, real-time score tracking, and persistent session statistics.",
                "bullet_2": "Implemented event-driven user input handling, conditional score evaluation algorithms, and animated visual feedback states.",
                "bullet_3": "Crafted a responsive UI with tactile micro-interactions and audio-visual cues, ensuring engaging cross-device interaction.",
                "image": "images/Rock Paper Scissor.png",
                "github_url": "https://github.com/GouravBerwal/Rock-Paper-Scissors",
                "order": 12,
            },
        ]
        for pdata in projects_data:
            Project.objects.create(**pdata)
        self.stdout.write(f"  ✓ {len(projects_data)} Projects seeded")

        # 4. Experiences (Chronological: Most Recent to Oldest)
        Experience.objects.all().delete()
        exp_data = [
            {
                "role": "Python Developer Intern",
                "company": "Alphawizz Technologies Pvt. Ltd",
                "company_url": "https://alphawizz.com/",
                "date_range": "August 2026 – Present",
                "logo": "images/alphawizz_logo.png",
                "is_right": False,
                "points": (
                    "Develop and maintain production backend features for web applications using Python and Django, configuring robust models, views, forms, and admin panel interfaces.\n"
                    "Build and integrate high-throughput RESTful APIs with Django REST Framework, covering serializers, viewsets, routing, and CRUD endpoints for 20+ modules.\n"
                    "Design and connect high-performance MySQL databases to the Django backend, architecting relational models and writing optimized ORM queries for low-latency data storage and retrieval.\n"
                    "Deploy Django applications and APIs to production on Render, configuring environment variables, security settings, and live database connections.\n"
                    "Collaborate cross-functionally using Git and GitHub for version control, structured code reviews, and agile issue tracking."
                ),
                "order": 1,
            },
            {
                "role": "Data Analytics & Business Development Intern",
                "company": "Younity.in",
                "company_url": "https://learn.younity.in/",
                "date_range": "March 2024 – May 2024",
                "logo": "images/younity_in_logo.jpeg",
                "is_right": True,
                "points": (
                    "Built automated performance analytics dashboards in Excel/Sheets, monitoring key growth KPIs, response times, and conversion funnels across 500+ client touchpoints.\n"
                    "Conducted in-depth cohort analysis and user interaction modeling using Python (Pandas), generating actionable business intelligence that increased conversion rates by 28%.\n"
                    "Automated weekly cross-functional reporting pipelines, reducing stakeholder manual analytical bandwidth by over 6 hours per week.\n"
                    "Awarded 'Top Communicator' and 'Best Decision Maker' honors for exemplary analytical rigor and data-driven executive presentations."
                ),
                "order": 2,
            },
            {
                "role": "Technical Operations & Process Specialist",
                "company": "TaskUs (Rangreza), Indore",
                "company_url": "https://www.taskus.com/",
                "date_range": "May 2023 – August 2023",
                "logo": "images/taskus_logo.jpeg",
                "is_right": False,
                "points": (
                    "Managed 100+ daily international technical chat interactions under stringent SLA guidelines, maintaining a consistent 98% Customer Satisfaction (CSAT) rating.\n"
                    "Analyzed edge-case failure logs and conducted root-cause analysis, partnering with engineering to patch documentation gaps and reduce repeat ticket escalations by 22%.\n"
                    "Leveraged quantitative metrics (FCR, ART, AHT) to optimize customer support triage workflows and improve overall operational throughput."
                ),
                "order": 3,
            },
            {
                "role": "Growth & Marketing Analytics Ambassador",
                "company": "Acmegrade",
                "company_url": "https://www.acmegrade.com/",
                "date_range": "May 2023 – July 2023",
                "logo": "images/acmegrade_logo.png",
                "is_right": True,
                "points": (
                    "Formulated data-driven acquisition and outreach strategies, evaluating conversion funnels and engagement metrics to maximize student enrollment ROI by 30%.\n"
                    "Analyzed multi-channel campaign performance using attribution modeling to identify high-converting student cohorts and optimize digital promotional spend.\n"
                    "Collaborated cross-functionally to streamline lead intake channels, slashing prospect response turnaround time by 45%."
                ),
                "order": 4,
            },
            {
                "role": "Campus Ambassador & Outreach Lead",
                "company": "TRYST, IIT Delhi",
                "company_url": "https://cap.trystiitd.org/",
                "date_range": "January 2023 – June 2023",
                "logo": "images/Tryst.jpeg",
                "is_right": False,
                "points": (
                    "Spearheaded regional campus outreach and digital marketing campaigns for North India's largest technical symposium, driving 150+ registrations.\n"
                    "Monitored and iterated campaign engagement analytics in real-time across institutional networks to maximize participant conversion and ROI.\n"
                    "Coordinated logistical and cross-functional operations with IIT Delhi student organizing committees, ensuring seamless event execution."
                ),
                "order": 5,
            },
            {
                "role": "Customer Operations Specialist",
                "company": "Teleperformance, Indore",
                "company_url": "https://www.tp.com/en-us/",
                "date_range": "February 2023 – April 2023",
                "logo": "images/Teleperformance.jpeg",
                "is_right": True,
                "points": (
                    "Handled high-volume customer interactions (120–150/day) under tight SLA turnaround times, achieving a 97% CSAT score and top performer ranking.\n"
                    "Identified recurring system defects and user friction points through structured log analysis, contributing to a 25% reduction in repeat tickets.\n"
                    "Honed analytical problem-solving, rapid technical troubleshooting, and high-pressure incident management."
                ),
                "order": 6,
            },
        ]
        for edata in exp_data:
            Experience.objects.create(**edata)
        self.stdout.write(f"  ✓ {len(exp_data)} Experience records seeded")

        self.stdout.write(self.style.SUCCESS("All portfolio data seeded successfully!"))

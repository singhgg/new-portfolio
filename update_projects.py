import re

with open('src/data/projects.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

index = content.find('const projects: Project[] = [')
if index != -1:
    new_projects = """const projects: Project[] = [
  {
    id: "mental-health",
    category: "Personal Project",
    title: "AI Mental Health / Mental Health Support System",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "#",
    github: "https://github.com/singhgg/mental-health-chatbot",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            AI Mental Health Support System
          </TypographyP>
          <TypographyP className="font-mono ">
            A personal project designed to provide mental health support through an AI-powered chatbot interface.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  },
  {
    id: "railway-management",
    category: "Personal Project",
    title: "Railway Management System",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "#",
    github: "https://github.com/GSriCharan12/Railway-Management-System",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            Railway Management System
          </TypographyP>
          <TypographyP className="font-mono ">
            A personal project to manage railway operations and bookings.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  },
  {
    id: "animation-website",
    category: "Personal Project",
    title: "Animation Website",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "#",
    github: "https://github.com/singhgg/css-animation",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            CSS Animation Website
          </TypographyP>
          <TypographyP className="font-mono ">
            A personal project focused on exploring and demonstrating various CSS animations.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  },
  {
    id: "solvencia",
    category: "Client Work",
    title: "Solvencia",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "https://solvencia.in/",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            Solvencia Client Website
          </TypographyP>
          <TypographyP className="font-mono ">
            A client website developed during professional work.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  },
  {
    id: "memories-unlimited",
    category: "Client Work",
    title: "Memories Unlimited",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "https://memoriesunlimited.in/",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            Memories Unlimited Client Website
          </TypographyP>
          <TypographyP className="font-mono ">
            A client website developed during professional work.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  },
  {
    id: "marcquity",
    category: "Client Work",
    title: "Marcquity",
    src: "/assets/projects-screenshots/portfolio/landing.png",
    screenshots: [],
    skills: { frontend: [], backend: [] },
    live: "https://marcquity.com/",
    get content() {
      return (
        <div>
          <TypographyP className="font-mono text-2xl text-center">
            Marcquity Client Website
          </TypographyP>
          <TypographyP className="font-mono ">
            A client website developed during professional work.
          </TypographyP>
          <ProjectsLinks live={this.live} repo={this.github} />
        </div>
      );
    },
  }
];

export default projects;
"""
    new_content = content[:index] + new_projects
    with open('src/data/projects.tsx', 'w', encoding='utf-8') as f:
        f.write(new_content)

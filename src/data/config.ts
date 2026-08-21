const config = {
  title: "Dhanwanth Singh | Full Stack Developer",
  description: {
    long: "Explore the portfolio of Dhanwanth Singh, a full-stack developer and creative technologist specializing in interactive web experiences, 3D animations, and innovative projects. Let's build something amazing together!",
    short:
      "Discover the portfolio of Dhanwanth Singh, a full-stack developer creating interactive web experiences and innovative projects.",
  },
  keywords: [
    "Dhanwanth Singh",
    "portfolio",
    "full-stack developer",
    "creative technologist",
    "web development",
    "3D animations",
    "interactive websites",
    "web design",
    "GSAP",
    "React",
    "Next.js",
    "Spline",
    "Framer Motion",
  ],
  author: "Dhanwanth Singh",
  email: "dhanwanthworks@gmail.com",
  site: "https://nareshkhatri.dev",

  // for github stars button
  githubUsername: "singhgg",
  githubRepo: "",

  get ogImg() {
    return this.site + "/assets/seo/og-image.png";
  },
  social: {
    linkedin: "https://www.linkedin.com/in/dhanwanth-singh/",
    github: "https://github.com/singhgg",
  },
};
export { config };

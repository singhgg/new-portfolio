import os

footer_path = r"C:\Users\ADMIN\Downloads\3d-portfolio-main1\3d-portfolio-main\src\components\footer\footer.tsx"
config_path = r"C:\Users\ADMIN\Downloads\3d-portfolio-main1\3d-portfolio-main\src\data\config.ts"

# Fix Footer
if os.path.exists(footer_path):
    with open(footer_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("async function CopyrightYear() {", "function CopyrightYear() {")
    with open(footer_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed footer.tsx")
else:
    print(f"File not found: {footer_path}")

# Fix Config
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('githubRepo: "3d-portfolio",', 'githubRepo: "",')
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed config.ts")
else:
    print(f"File not found: {config_path}")

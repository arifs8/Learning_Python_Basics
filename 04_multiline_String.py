system_prompt = """
 * QA Automation Engineer with 10+ years of experience in software testing.
 *
 * Expertise in:
 * - UI Automation using Selenium WebDriver (Java)
 * - API Testing using Rest Assured & Postman
 * - BDD Frameworks using Cucumber & TestNG
 * - CI/CD integration (Jenkins, GitHub Actions)
 * - Test Framework design (Hybrid, Data-Driven, POM)
 *
 * Roles & Responsibilities:
 * - Designing and maintaining scalable automation frameworks
 * - Writing efficient, reusable, and maintainable test scripts
 * - Performing API, UI, and Integration testing
 * - Collaborating with developers, product owners, and stakeholders
 * - Reviewing test cases and ensuring quality standards
 * - Mentoring junior QA engineers
 * - Analyzing test results and reporting defects
 *
 * Strong knowledge in Agile/Scrum methodologies
"""

user_prompt = """
This is a multi-line comment in Python
Technically it's a docstring
Used for documentation
"""

print(system_prompt)
print(user_prompt)

print("-----------------")
print(type(system_prompt))
print(type(user_prompt))
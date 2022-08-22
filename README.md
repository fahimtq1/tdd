# Test Driven Development Basics

## Definition of Test Driven Development (TDD)

TDD is the software development practice of creating unit tests before producing the actual code of a program. In this way, the tests are given priority, thus the tests themselves drive development. It's roots are derived from the Agile Manifesto, as can be seen in its iterative nature and other principles that will be covered below.

### Definition of Unit Testing?

Unit testing is a software development practice, in which the smallset testable parts are independently tested to ensure they are fit for use. 

## Red, Green, Refactor

There are five parts to TDD lifecycle:

1. Red
- The developer needs to know what they want to test and what to expect from the functionality that they is being tested
- This stage checks the accuracy of the developer's understanding of the business logic
- The test case is written by relying on use case and user stories
- A good test can be used as a form of business documentation that can be used to validate the application logic

2. Green
- Begin building the code for the application
- Write the least amount needed to pass the unit test
- The code doesn't need to be extensive, as it should only be sufficient to pass the test

3. Refactor
- Check for redundancies in the code and potential code optimisations 
- Maintain the same standard for the test code and production code

## Advantages of TDD

- Ensures the code is clean and only the sufficient amount of code required for the application logic is used

## Disadvantages of TDD

- Time consuming process

## How to run tests in the terminal:

```python -m pytest -v```

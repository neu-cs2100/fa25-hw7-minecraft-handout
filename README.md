# Homework 7

## Learning Outcomes

- Writing classes and interfaces
- Following a UML diagram
- Using the `super` keyword
- Practicing encapsulation

Based on this existing assignment written by Prof. Ellen Spertus in Java:

## Introduction

The learning goals of this assignment are:

- Creating a class in Java, including
 - using instance variables
 - writing getters
 - overriding equals() and toString()
 - writing other methods
 - using the visibility modifiers public and private
- Correctly performing arithmetic on integers
- Building up strings with String.format()
- Doing the following within IntelliJ
 - generating javadoc
 - running checkstyle
 - creating and running tests
 - measuring coverage
- Practicing test-driven development
- Practicing using git and GitHub

While working on the assignment, keep track of time spent, sources used, and bugs found by (or in) tests.

Here are questions it would be appropriate to ask AI (or a search engine):

- How do I wrote a good unit test?
- How do I debug a failing unit test?
- How should I compare strings in Java?

It would not be appropriate to provide an AI with the javadoc and ask it to generate code or tests.

Remember: You won't have AI help on the quizzes or in your co-op interviews.

## Preparation
The Learn CS Online lessons (linked in [Resources for Learning Java](https://northeastern.instructure.com/courses/202024/modules/1464167) will help prepare you for this assignment and Quiz 1. The fourth lesson, [Creating Classes](https://www.learncs.online/lessons/java/kotlin_to_java_creating_classes), is most relevant.

## Setup
Accept the assignment from
In IntelliJ, create a new project using that Git repo (File -> New -> Project from version control)

## Run Checkstyle

(Video)

1. Set up the Checkstyle plugin to use the provided fundies2-checks.xml
2. Run Checkstyle from within IntelliJ, as shown in the video. You should see 4 errors. Fix them by making the instance variables private.
3. Rerun Checkstyle to make sure you have fixed all the errors.
4. Add and commit your changes with the message "Fix checkstyle errors".
5. Push your changes back to Github.

Warning: You might get errors from the Checkstyle plugin. You can ignore them.

Note: When your code has a style error, IntelliJ may suggest suppressing the warning. Never accept this option, since it defeats the purpose of running Checkstyle (and won't fool the autograder).

## Generate and Modify Javadoc

This video demonstrates all the steps for this section.

(Video)

1. Open a terminal window and cd to the directory with the project.
2. Create a direction (with mkdir) named docs.
3. Back in IntelliJ, select Tools > Generate JavaDoc...
4. Make sure "Include test sources" is unchecked. (See picture below.)
5. Check "Include JDK and library sources in -sourcepath".
6. For the output directory, specify the directory you created.
7. Check the box for @author.
8. Make sure the box is checked for "Open generated documentation in browser".
9. Click on Generate.

(Image)

10. If everything worked, that should pop open a browser with the generated javadoc. Navigate around it.
11. Go back to the source code, aind the existing @author tag.
12. Add another @author tag on the next line with your name.
13. Regenerate the javadoc and find your name.
14. Read through the javadoc to see how each method should behave.
15. Add, commit, and push your changes, with the commit message "Add self as author in javadoc". 

## Write Tests

Follow the instructions in the video to see how to create and run tests. 

Next, create one or more tests for each of the following methods:

- getName()
- getMaxHealth()
- getHealth()
- toString()
- equals()
- isInjured()
- isAlive()
- takeDamage()
- getCurrentStrength()

We provide tests of attack().

You will need enough tests for each method for every path through the code. Test names must:

- start with the name of the method under test
- be descriptive

For example, good names for tests of toString() would be:

- toStringWorksWhenHealthy
- toStringWorksWhenInjured
- toStringWorksWhenDead

Do not write tests for hashCode(), narrateBattle(), and main(). While it is possible to [test methods with output](https://www.baeldung.com/java-testing-system-out-println), we will not be doing so.

Be sure to add, commit, and push before proceeding to the next step. Feel free to do so more than once.

## Implement Mob

Commit and push your changes after doing significant work. For now, don't worry about making your code elegant. You'll have a chance to improve it later.

1. Some of the instance variables are never changed after being initialized in the constructor. Make those instance variables final (the equivalent of Kotlin's val).
2. Implement the methods that you wrote tests for.
3. Watch the below video before implementing attack().

(Video)

## Test and Debug

1. Run your tests. Note in Summary.md how many tests pass and how many fail on your first attempt and whether the bugs were in your tests or in the methods under test.
2. Debug your code and tests. See videos below on how to use the debugger.
3. Check your code coverage, as shown in the below video. Add tests until you get 100% coverage

(3 videos)

Be sure to commit and push your changes at least once during this stage.

## Refactor

Now, go back and clean up your code. Replace any use of string concatenation with calls to String.format(). You can make changes with confidence because:

- you have tests
- you can go back to prior versions if necessary

We haven't yet taught how to use git to revert to prior versions of your code. For now, use Github to browse and copy old code if it is needed.

Be sure to fix any checkstyle errors.

## Use the Autograder

Upload your work in progress to Gradescope. The autograder will:

- run Checkstyle
- run our tests against your code (as on Homework 1)
- run your tests against instructor-written code that
 - we believe is correct
 - we know to be buggy

To get full credit, your tests must:

- not report any errors in our correct code (unless, of course, it isn't actually correct)
- report all errors in our buggy code
- have names that start with the methods they are testing

For example, you would not get credit for catching bugs in toString() if the names of those tests do not start with "toString".

This video explains autograder results.

(Video that Ellen marked as worth redoing)

## Complete Submission

Complete Summary.md and make a final submission.

## Grading Guide

This may be adjusted:

- Autograder: 65
 - Checkstyle: 5
 - Student code passes our tests: 20
   - Getters: 1
   - toString: 3
   - equals: 3
   - isInjured: 2
   - isAlive: 2
   - takeDamage: 2
   - getCurrentStrength: 3
   - attack: 4
 - Student code passes student tests: 10
 - Student tests do not report bugs in correct* instructor code: 10
 - Student tests do report bugs in buggy instructor code: 15
 - Coverage: 5
- Summary.md: 10
- Code quality: 15
 - Using String.format() instead of string concatenation in Mob: 3 [many students lost these points last year]
 - Test names make clear what is being tested: 2 [many students lost these points last year]
 - Tests are split across multiple methods: 2
 - Behavior of tests does not depend on the order in which they are run: 3
 - No redundant/unneeded code: 3
 - Language features are used appropriately: 2
- Git usage: 10
 - Writing and committing tests before implementing Mob.java: 5 [many students lost these points last year]
 - Correct use of add, commit, push: 5

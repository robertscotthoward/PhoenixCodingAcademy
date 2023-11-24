[TOC]

# Overview

You use:

* **Programming languages** to tell a computer what to do.
* **User stories** to tell people what you want.

The modern format for programming teams is with **User Stories** that together define a [Software Process Specification (SPS)](/subjects/softeng_specification).
Each user story has three main parts:

* Title - a short string that appears in a table
* Description - the user story format: "WHO wants WHAT WHY"
* Acceptance Criteria - the Gherkin statements.


The description defines "WHO wants WHAT WHY" first, and then is follow by more details if needed. The WHO is the customer, who is likely paying you money. But that customer works in an business so WHAT they want must be justified by business with a WHY. And there is likely a higher up person in that business that makes sure that the WHAT and WHY will save the business money, because it certainly will cost the business to implement that user story.

The description is typically written in this format first:

```
As a ROLE, I want WHAT so that I can WHY.
```

Example:
```
As a parent, I want my trash taken periodically out so that it doesn't stink up the kitchen or overflow.
```

The "Acceptance Criteria" (AC) is written in a modern popular format called Gherkin, that is often used to ensure that the readers build what the writer wants. You think like a lawyer in that you try to imagine all the ways someone might misinterpret what you wrote, and then rewrite it so that they do not.

# Details

User Stories in Gherkin format appear as one or more sentences where the first word in each sentence must only start with one of the following allowed words, which are capitalized so that they stand out:

* SCENARIO - the name of the user story. Can be used by other user stories.
* GIVEN - the starting state of the user story
* WHEN - a condition for an event to happen
* THEN - what happens next
* AND - used to keep sentences from getting long
* BUT - same as AND but might be more readable in certain cases

The word "OR" can appear in a sentence, but not start a sentence.


## Examples

```
SCENARIO 1 - take out trash
GIVEN I am in the kitchen
AND I look in the trash can
THEN I see that there is little or no trash

```

Example from [website](https://learndevtestops.com/2020/07/15/my-approach-for-writing-e2e-scenarios-using-gherkin/)
![Gherkin Example 1](/projects/web/static/images/gherkin1.png)


# References

* [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
* [Gherkin: Overview, Use Cases, and Format]](https://www.ranorex.com/blog/gherkin-overview-use-cases-and-format/)
* [How to Write Better User Stories With Gherkins (Template Included)](https://userpilot.com/blog/user-stories-templates/)
* [Gherkin Language: Format, Syntax & Gherkin Test in Cucumber](https://www.guru99.com/gherkin-test-cucumber.html)
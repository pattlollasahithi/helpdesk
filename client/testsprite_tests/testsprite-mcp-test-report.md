# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** EduReach client (`edureach_college_help_desk_agent/client`)
- **Date:** 2026-10-14
- **Prepared by:** TestSprite AI Team
- **Test Scope:** Full frontend codebase
- **Local App:** Vite dev server at `http://localhost:5174/`
- **Backend:** Express API at `http://localhost:5000` (used by chat)

---

## 2️⃣ Requirement Validation Summary

### Requirement: Homepage Marketing Content
- **Description:** Visitors can load `/`, see the EduReach hero and campus branding, jump to programs, and scroll through about, courses, mentors, campus, placements, and footer.

#### Test TC001 View the homepage hero and branding
- **Test Code:** [TC001_View_the_homepage_hero_and_branding.py](./TC001_View_the_homepage_hero_and_branding.py)
- **Test Error:** TEST BLOCKED — homepage SPA did not initialize; blank viewport with only a root `<div>` and `<script>`.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/2cabfd41-0d92-45bd-8a75-47ea1accc737
- **Status:** BLOCKED
- **Severity:** HIGH
- **Analysis / Findings:** This is an infrastructure failure, not a confirmed UI bug. The tunnel lost `127.0.0.1:5174` (`ECONNREFUSED`) during the run. Re-run after keeping Vite bound with `--host 127.0.0.1 --port 5174`.
---

#### Test TC003 Jump to programs from the hero
- **Test Code:** [TC003_Jump_to_programs_from_the_hero.py](./TC003_Jump_to_programs_from_the_hero.py)
- **Test Error:** TEST BLOCKED — `Explore Programs` was not found because the homepage never rendered.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/4586d16a-10d7-4a27-b2ff-df491b394b2b
- **Status:** BLOCKED
- **Severity:** HIGH
- **Analysis / Findings:** Code has an `#courses` CTA in `HeroSection.jsx`. The test could not click it because the remote browser saw a blank page. Not evidence that the CTA is missing.
---

#### Test TC006 Scroll through the full homepage content
- **Test Code:** [TC006_Scroll_through_the_full_homepage_content.py](./TC006_Scroll_through_the_full_homepage_content.py)
- **Test Error:** TEST BLOCKED — site unavailable after reloads; About and footer never appeared.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/f76cb499-fd05-44b2-b260-69dac9034407
- **Status:** BLOCKED
- **Severity:** HIGH
- **Analysis / Findings:** Same tunnel/dev-server drop. Homepage sections exist in `HomePage.jsx`; they were not validated in this run.
---

### Requirement: Sticky Navbar Navigation
- **Description:** Persistent header with logo, section links, mobile hamburger, and UI-only Login/Sign Up buttons.

#### Test TC004 Use the sticky navigation to jump between sections
- **Test Code:** [TC004_Use_the_sticky_navigation_to_jump_between_sections.py](./TC004_Use_the_sticky_navigation_to_jump_between_sections.py)
- **Test Error:** TEST BLOCKED — navbar never appeared on a blank `http://localhost:5174/`.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/e9f29034-1cde-4d56-8986-e3bd877e3091
- **Status:** BLOCKED
- **Severity:** HIGH
- **Analysis / Findings:** `Navbar.jsx` renders Home/About/Courses/Mentors/Campus/Placements. Hash links were not exercised because the SPA did not mount.
---

#### Test TC008 Open and close the mobile navigation menu
- **Test Code:** [TC008_Open_and_close_the_mobile_navigation_menu.py](./TC008_Open_and_close_the_mobile_navigation_menu.py)
- **Test Error:** TEST BLOCKED — no hamburger control on a blank page.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/b9f69a47-8864-44c8-b04c-9927ed925342
- **Status:** BLOCKED
- **Severity:** MEDIUM
- **Analysis / Findings:** Mobile menu is implemented (`md:hidden` hamburger). Viewport-level verification still needs a live render.
---

#### Test TC009 Keep the homepage open when using the logo and auth buttons
- **Test Code:** [TC009_Keep_the_homepage_open_when_using_the_logo_and_auth_buttons.py](./TC009_Keep_the_homepage_open_when_using_the_logo_and_auth_buttons.py)
- **Test Error:** TEST BLOCKED — no EduReach logo, Login, or Sign Up controls.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/0553a5e0-1dba-4054-b492-4d1737c7eeb1
- **Status:** BLOCKED
- **Severity:** MEDIUM
- **Analysis / Findings:** Login and Sign Up are UI-only buttons with no routes. That is a known product limitation, but this test did not reach those buttons.
---

### Requirement: Help Desk Chat
- **Description:** Floating button opens EduReach Bot. Visitors send custom questions or quick chips and get a backend reply; they can minimize, close, and keep browsing.

#### Test TC002 Send a custom question to the help-desk chat
- **Test Code:** [TC002_Send_a_custom_question_to_the_help_desk_chat.py](./TC002_Send_a_custom_question_to_the_help_desk_chat.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/35965439-bce7-4b12-8c92-f94a2d511f21
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Custom message send works end to end against `/api/chat/message` while the client and API were reachable. User message and bot reply both showed.
---

#### Test TC005 Read quick question replies in the chat drawer
- **Test Code:** [TC005_Read_quick_question_replies_in_the_chat_drawer.py](./TC005_Read_quick_question_replies_in_the_chat_drawer.py)
- **Test Error:**
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/c5702bde-14e0-4982-b5d0-45c35e158930
- **Status:** ✅ Passed
- **Severity:** LOW
- **Analysis / Findings:** Opening chat, reading the welcome message, and using a quick-question chip produced a bot reply. Core help-desk path is working.
---

#### Test TC007 Minimize and reopen the chat without losing the conversation
- **Test Code:** [TC007_Minimize_and_reopen_the_chat_without_losing_the_conversation.py](./TC007_Minimize_and_reopen_the_chat_without_losing_the_conversation.py)
- **Test Error:** TEST BLOCKED — SPA blank; `127.0.0.1:5174` returned `ERR_EMPTY_RESPONSE`.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/74268ea9-375e-4634-8e38-48917e17cf36
- **Status:** BLOCKED
- **Severity:** MEDIUM
- **Analysis / Findings:** Closing the drawer unmounts it (`if (!open) return null`), so conversation state is lost on reopen. That is a real product risk, but this run never reached the UI to confirm it.
---

#### Test TC010 Close the chat drawer and return to browsing
- **Test Code:** [TC010_Close_the_chat_drawer_and_return_to_browsing.py](./TC010_Close_the_chat_drawer_and_return_to_browsing.py)
- **Test Error:** TEST BLOCKED — floating chat button never appeared.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/d16c8b29-7e21-49d0-a668-960aa6810fe7
- **Status:** BLOCKED
- **Severity:** MEDIUM
- **Analysis / Findings:** Close/minimize handlers exist in `ChatDrawer.jsx`. Not validated because the page did not render.
---

#### Test TC011 Stay on the homepage when opening navigation after chat use
- **Test Code:** [TC011_Stay_on_the_homepage_when_opening_navigation_after_chat_use.py](./TC011_Stay_on_the_homepage_when_opening_navigation_after_chat_use.py)
- **Test Error:** TEST BLOCKED — no chat button or nav links on a blank viewport.
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/50ec55a9-4536-5a1f-9948-a9eb664246ae/test/cc5855f1-3323-4f74-8370-383ade1565bf
- **Status:** BLOCKED
- **Severity:** MEDIUM
- **Analysis / Findings:** Combined chat + nav flow was not executed. Re-run after the local Vite process stays up for the full suite.
---

## 3️⃣ Coverage & Matching Metrics

- **18.18% of tests passed** (2 of 11)
- **0 failed** as functional defects
- **9 blocked** due to local server / tunnel unavailability

| Requirement                 | Total Tests | ✅ Passed | ❌ Failed | BLOCKED |
|-----------------------------|-------------|-----------|-----------|---------|
| Homepage Marketing Content  | 3           | 0         | 0         | 3       |
| Sticky Navbar Navigation    | 3           | 0         | 0         | 3       |
| Help Desk Chat              | 5           | 2         | 0         | 3       |
| **Overall**                 | **11**      | **2**     | **0**     | **9**   |

---

## 4️⃣ Key Gaps / Risks

> 18.18% of tests passed fully. Most homepage and navigation cases were blocked because the Vite process on port 5174 dropped while TestSprite tunneled to it (`ECONNREFUSED` / blank SPA). The two tests that ran while the app was up both passed, and both were chat flows.

Risks and follow-ups:
- Keep the client running with `npx vite --port 5174 --host 127.0.0.1` (or a production `vite preview`) for the full TestSprite session; the first `npm run dev` instance did not stay reachable.
- Login and Sign Up are visual-only; there is no auth route or API.
- Chat drawer unmounts on close, so conversation history is likely discarded — confirm on a healthy re-run (TC007).
- Chat depends on the backend at `http://localhost:5000/api/chat/message`; keep that API up whenever re-running help-desk tests.
- Prefer production preview for fuller TestSprite coverage (dev mode is capped and less stable under tunnel load).
---

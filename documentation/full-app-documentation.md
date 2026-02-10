# Neomi — Complete App Documentation

## 1. What Is Neomi?

Neomi is a minimalist iOS habit tracking app built for people who want to build and maintain positive habits across every area of their life. It covers physical exercise, mental growth, creative practice, and everyday responsibilities — all in one place.

The core idea is simple: you schedule habits, track them with a timer, and earn points for everything you complete. Over time, your points accumulate into a visual graph that shows your progress, and streaks keep you motivated to stay consistent.

Neomi is designed to feel premium and satisfying. Every interaction — from starting a timer to completing an activity — is accompanied by smooth animations and haptic feedback. The interface is clean, spacious, and distraction-free. It's built to make you want to open it, not dread it.

The app is iPhone-only, requires iOS 18.0 or later, and is developed by STNG Studios (Denmark).

---

## 2. Getting Started

### Signing In

Neomi uses Apple Sign In as its only authentication method. When you first open the app, you see a welcome screen with the Neomi logo (a large "N" in a circle), a "Welcome to Neomi" headline, and four benefit descriptions:

- Track habits across all areas of life
- Visualize your progress over time
- Stay motivated with reminders
- Sync across all your devices

Below this is the native Apple Sign In button. Tapping it authenticates you with your Apple ID — your name and email are pulled from Apple automatically.

### Onboarding

After signing in, you go through an 8-step onboarding flow with a progress bar at the top showing "Step X of Y":

1. **Categories Selection** — Choose which habit categories interest you (Physical, Mental, Creative, Everyday)
2. **Goals Selection** — Set your initial goals and intentions
3. **Physical Habits Selection** — Pick which physical activities you want to track
4. **Mental Habits Selection** — Pick which mental activities you want to track
5. **Creative Habits Selection** — Pick which creative activities you want to track
6. **Everyday Habits Selection** — Pick which everyday activities you want to track
7. **Personal Info** — Enter any additional personal details
8. **Week Preview** — See a preview of what your first week will look like

Each step has Back/Next buttons, and some steps can be skipped. After the final step, a subscription paywall appears before you enter the main app.

---

## 3. Subscription

Neomi has no free tier — a subscription is required to use the app.

### Plans

| Plan | Price | Free Trial | Savings |
|------|-------|------------|---------|
| Monthly | $4.99/month | 3-day free trial | — |
| Yearly | $39.99/year | 7-day free trial | 33% off |

### What's Included (All Features)

- Unlimited habit tracking across all categories
- Advanced analytics and progress visualization
- Smart reminders and notifications
- Cloud sync across devices
- Focus Mode (coming soon)
- Social features (coming soon)

The subscription screen shows these features with icons, lets you toggle between monthly and yearly plans, and has a prominent "Start Free Trial" button. You can restore purchases, and links to Terms of Service and Privacy Policy are at the bottom.

Your active subscription is visible on the Profile screen as a badge showing the plan type and days remaining.

---

## 4. The Home Screen

The Home screen is the main dashboard — everything you need for your daily habit tracking lives here. It's a vertical scrollable layout with the following sections from top to bottom:

### Points Graph

At the very top is an interactive line chart showing your cumulative points over time, styled like a stock chart with smooth curves and a gradient fill beneath the line. Your total points appear in the header.

Five time period buttons let you switch the view:
- **Week** — Daily points for the current week
- **Month** — Daily points for the current month
- **This Year** — Monthly aggregates for the calendar year
- **Year** — Monthly aggregates for the trailing 12 months
- **All Time** — Your entire history

You can tap and drag on the chart to see the exact point value at any date — a floating bubble appears with the number, and a vertical line marks the position.

When you have no data yet, it shows: "Complete activities to see your progress."

### Daily Progress Ring

Below the graph is a circular donut-style progress ring showing how many of today's todos you've completed (e.g., "3/5" in the center). The ring is color-coded:
- **Green segments** — Completed activities
- **Gray segments** — Remaining activities

Below the ring it shows "X points today" — your total points earned for the current day.

### Week Navigation

A horizontal row of date buttons showing the current week. The current day is highlighted. You can tap any date to view that day's todos and stats. This lets you look back at what you completed on previous days or see what's scheduled ahead.

### Todo List

The main content area shows your scheduled habits for the selected day as a vertical list of cards. Each card represents one todo and changes appearance based on its status:

- **Pending** (today) — Full-color card with the category's groove color as background. Shows the activity icon in a circle, the activity name, and the target duration. Has action buttons to start the appropriate activity mode, plus a skip button.

- **In Progress** — Shows elapsed time vs. target time with a progress circle filling up. Has a resume button to reopen the activity mode view.

- **Ready to Complete** — The timer has finished but the activity hasn't been confirmed yet. Shows a prompt to complete.

- **Completed** — Greyed-out card with a green checkmark. Non-interactive. Moves to the bottom of the list.

- **Skipped** — Greyed-out card with a forward icon. Non-interactive.

- **Missed** — Card with a warning triangle. Shown for activities that weren't completed by midnight.

- **Future Date** — Simplified, non-interactive card for activities scheduled on dates you're previewing ahead.

Only one activity can be active at a time — if you try to start a second one, an alert tells you to finish or cancel the current one first.

### Add Button

A floating circular "+" button sits in the bottom-right corner, above the tab bar. Tapping it opens the Add Habit sheet. The button only appears when you're on the Home tab and subtly moves when you scroll.

---

## 5. The Four Habit Categories

Neomi organizes all habits into four color-coded categories. Each category has a base color, a lighter "groove" shade (used for card backgrounds), and an even lighter "icon circle" shade.

### Physical (Red)

Activities focused on bodily health and exercise:

| Activity | Tracks | Points | Interval |
|----------|--------|--------|----------|
| Run | Duration + Distance | 6 points | per 10 min |
| Cycle | Duration + Distance | 4 points | per 10 min |
| Walk | Duration + Distance | 2 points | per 10 min |
| Workout | Duration | 4 points | per 10 min |
| Yoga | Duration | 5 points | per 10 min |
| Stretch | Duration | 5 points | per 5 min |
| Swim | Duration + Distance | 7 points | per 10 min |

### Mental (Blue)

Activities focused on cognitive growth and mindfulness:

| Activity | Tracks | Points | Interval |
|----------|--------|--------|----------|
| Meditation | Duration | 10 points | per 10 min |
| Reading | Duration + Pages | 5 points | per 10 min |
| Learning | Duration | 5 points | per 10 min |
| Puzzles | Duration | 5 points | per 10 min |

### Creative (Purple)

Activities focused on artistic expression and creation:

| Activity | Tracks | Points | Interval |
|----------|--------|--------|----------|
| Music & Production | Duration | 5 points | per 10 min |
| Drawing/Painting | Duration | 5 points | per 10 min |
| Writing | Duration | 5 points | per 10 min |
| Photography & Editing | Duration | 5 points | per 10 min |

### Everyday (Teal)

Activities focused on daily responsibilities and productivity:

| Activity | Tracks | Points | Interval |
|----------|--------|--------|----------|
| Cleaning | Duration | 5 points | per 10 min |
| Homework | Duration | 5 points | per 10 min |
| Deep Work | Duration | 5 points | per 10 min |
| Cooking | Duration | 5 points | per 10 min |
| Laundry | Loads (quantity) | 15 points | per load (50 min/load) |
| Gardening | Duration | 5 points | per 10 min |

**Special note on Laundry:** Unlike all other activities, Laundry is quantity-based (loads) rather than purely duration-based. Each load takes 50 minutes and earns 15 points. Laundry can also run concurrently with other activities — you can start a laundry load and then do a meditation session at the same time.

---

## 6. Adding a Habit

Tapping the "+" button on the Home screen opens the Add Habit sheet. This is a two-screen flow with a smooth morph animation between them.

### Screen 1: Habit Selection Grid

At the top are four category tabs (Physical, Mental, Creative, Everyday), shown as icon-only pill buttons colored in their category color. The selected tab is highlighted with a solid color; others are at 15% opacity.

Below the tabs is a 2-column grid of habit cards for the selected category. Each card shows the habit's icon and display name. Tapping a card triggers a matched geometry animation — the card expands and morphs into the detail configuration screen.

### Screen 2: Habit Configuration

The selected habit's card expands into a large header with the icon and name on the category's color background. Below it are the configuration options:

**Duration / Quantity Setting**
- For most habits: A stepper to set the target duration (5–120 minutes, in 5-minute steps)
- For Laundry: A stepper to set the number of loads (1–10), with a conversion shown (e.g., "3 loads = 150 min")

**Scheduling Options**

You choose one of two paths:

**"Just Today"** — Adds a single todo for today only. No recurrence. This is the default.

**"Schedule"** — Opens scheduling controls:
- **Recurring toggle** — Enables weekly recurrence
- **Quick-select buttons**: "Every Day" (all 7 days) or "Week Days" (Mon–Fri)
- **Day-of-week buttons**: M, T, W, T, F, S, S — tap to toggle individual days on/off. Selected days are highlighted in the category color.
- **Calendar button** — Opens a full multi-date calendar picker where you can select specific dates. If recurring is on, the app infers monthly patterns (e.g., "1st Monday of each month"). If recurring is off, it creates individual one-time todos for each selected date.

**Add Button**

The button text changes based on what you've configured:
- "Add to Today" — one-time, today only
- "Add Recurring Activity" — weekly recurrence on selected days
- "Add Monthly Activity" — monthly ordinal pattern (e.g., 2nd Wednesday)
- "Add to X Dates" — specific calendar dates, non-recurring

A back arrow returns to the grid, and a cancel button closes the entire sheet.

---

## 7. Activity Modes — How You Track

When you start a todo from the Home screen, a full-screen activity mode opens. The mode that opens depends on the habit type. All modes share some common elements — a timer, the category's color as the background, and a finish button — but each is tailored to its activity.

### Generic Timer Mode

**Used for:** Run, Cycle, Walk, Swim, Yoga, Stretch, Puzzles, Cooking, Gardening

This is the default mode for most activities. The entire screen fills with the category's color, creating an immersive, focused experience.

**What you see:**
- A large circular progress ring (220pt diameter) in the center
- The elapsed time displayed in large monospaced text (MM:SS or HH:MM:SS) inside the ring
- The target duration shown below (e.g., "10 min target")
- The activity icon and name beneath the timer
- A white "Finish [Activity Name]" button at the bottom

**How it works:**
- The timer counts **up** from zero — not down from the target. This is intentional: you're encouraged to do as much as you can, and the target is a milestone, not a deadline.
- When you reach the target, a green checkmark appears with "Target reached!" and a celebration haptic fires. But the timer keeps running — you can continue as long as you want.
- The progress ring fills from 0% to 100% as you approach your target, then stays full.
- You finish when you're ready by tapping the "Finish" button.

**Navigation controls:**
- **Collapse button** (chevron down, top-left) — Minimizes the mode without canceling. Your timer keeps running. You can return to it from the Home screen.
- **Cancel button** (top-right) — If you've been going for more than 60 seconds, a confirmation dialog appears: "You have X minutes of progress. Are you sure you want to cancel?" with "Cancel Session" and "Continue" options. If under 60 seconds, it cancels immediately.

### Workout Mode

**Used for:** Workout

A specialized mode for strength training and exercise sessions that combines a timer with detailed exercise logging.

**What you see:**
- A smaller timer ring (180pt) at the top showing elapsed time and a "Workout Session" label
- An exercise count below the timer (e.g., "3 exercises logged")
- A scrollable list of logged exercises in the middle
- An "Add Exercise" button (white bar with plus icon)
- A "Finish Workout" button at the bottom

**Exercise logging flow:**
1. Tap "Add Exercise" to open the Exercise Search view
2. Search or browse exercises by name, category (strength, cardio, flexibility, balance), muscle group (chest, back, legs, shoulders, arms, core, full body), or equipment type (barbell, dumbbells, machine, cables, bodyweight)
3. Favorite exercises appear with a star — tap the star to favorite/unfavorite for quick access later
4. Select an exercise to add it to your workout
5. For each exercise, you can log multiple sets with reps and weight
6. Each set has a checkbox to mark it as complete
7. You can add or remove sets as needed

**Personal records:** The app tracks your personal records (PRs) for each exercise — heaviest weight, most reps, most volume (weight x reps). When you beat a PR, it's flagged.

**Exercise history:** You can view past performances of any exercise to see your progression over time, including last weight, last reps, and when you last performed it.

### Task Mode

**Used for:** Deep Work, Homework, Learning, Writing, Music & Production, Drawing/Painting, Photography & Editing, Gardening

A mode designed for productivity-focused activities where you work through a checklist of tasks.

**What you see:**
- A timer ring at the top showing elapsed time
- A task progress indicator: "X/Y tasks (Z%)"
- A collapsible "Previous Tasks" section (if there are unfinished tasks from earlier sessions)
- A scrollable task checklist
- An "Add Task" button that opens a small input sheet
- A "Finish" button at the bottom

**Task management:**
- Add tasks with custom titles (the placeholder text adapts to the activity type, e.g., "Add a focus goal..." for Deep Work)
- Tap the checkbox next to a task to mark it complete
- Delete tasks you no longer need
- Tasks are specific to the activity session

**Task carry-over:** If you finish a session with uncompleted tasks, those tasks are saved. The next time you start the same activity, they appear in a collapsible "Previous Tasks" section at the top. You can carry over individual tasks or all of them at once with a "Carry Over All" button.

### Cleaning Mode

**Used for:** Cleaning

A mode with a timer and a checklist of predefined cleaning areas.

**What you see:**
- A smaller timer ring (180pt) showing elapsed time
- An "X areas cleaned" counter
- A scrollable list of 10 cleaning area cards, each with a name, icon, and toggle checkbox:
  1. Kitchen
  2. Bathroom
  3. Bedroom
  4. Living Room
  5. Office
  6. Hallway
  7. Garage
  8. Dining Room
  9. Laundry Room
  10. Other
- A "Finish Cleaning" button at the bottom

Toggle areas on and off as you clean them. The counter updates in real time.

### Meditation Mode

**Used for:** Meditation

A calming, focused mode designed for mindfulness practice.

**What you see:**
- A large timer progress ring with thin, serene font styling
- "Target reached!" indicator when your target is met
- A breathing guide section with a large semi-transparent brain icon
- Motivational prompts:
  - "Focus on your breath"
  - "Let your thoughts pass like clouds"
- A "Finish Meditation" button at the bottom

**On completion:** When you tap "Finish Meditation," a sheet appears asking you to:
- Rate your mood on a 1–5 scale
- Add optional notes about the session
- See a summary of your elapsed time

### Reading Mode

**Used for:** Reading

A mode tailored for book tracking alongside timed reading sessions.

**What you see:**
- A timer display showing elapsed reading time
- Input fields for:
  - Book title (optional)
  - Author (optional)
  - Start page
  - End page (updated during or after the session)
  - Notes field
- A "Continue Last Book" button if you've read before (pulls up your last book's title and page)
- A "Finish Reading" button

**Book history:** The app remembers your books — it stores the last page you were on for each title. When you start a new reading session, you can continue where you left off. Pages read are calculated automatically (end page minus start page).

You can update the book info and page numbers while the timer is running.

---

## 8. The Points System

Points are the core gamification mechanic in Neomi. Every activity you complete earns you points, and those points accumulate to show your overall progress.

### How Points Are Calculated

The formula is:

```
Points = (Elapsed Minutes / Interval Minutes) x Points Per Interval
```

The result is rounded to the nearest whole number.

**Example calculations:**
- **30-minute run** → 30 / 10 x 6 = **18 points**
- **20-minute meditation** → 20 / 10 x 10 = **20 points**
- **7-minute stretch** → 7 / 5 x 5 = **7 points**
- **2 loads of laundry** → 2 x 15 = **30 points**
- **5-minute run** → 5 / 10 x 6 = **3 points**

### Partial Completion

You always get credit for the time you put in. If your target is 30 minutes but you only do 15, you earn half the points. There's no penalty for stopping early — any time invested counts. The minimum is 1 minute of elapsed time.

### Where Points Appear

- **Home screen**: Points graph (cumulative over time) and "X points today" below the daily progress ring
- **Stats screen**: Total points, daily average, best day, category breakdown, and points over time graph
- **Profile screen**: Lifetime total points in the stats summary

### Points Are Earned Immediately

Points are credited the moment you finish an activity — there's no delay or batch processing. The points graph and daily total update instantly.

---

## 9. The Stats Screen

The Stats screen (second tab) is your analytics dashboard. It provides a comprehensive view of your progress across multiple visualizations.

### Time Period Selector

Four buttons at the top: **Week**, **Month**, **Year**, **All Time**. Switching the period updates all components below.

### Stats Overview Cards

**Total Points Card** (large) — Shows your total points for the selected period with a small bar chart of recent daily points (last 7 days).

**Three Mini Cards** in a row:
- **Activities** — Number of completed activities, with a mini pie chart showing category distribution
- **Daily Average** — Average points earned per day in the period
- **Best Day** — Highest single-day points, with a "Record" badge if it's your all-time best

### Category Breakdown

A pie or donut chart showing how your points are distributed across the four categories. Each segment is colored in the category's color and shows the percentage. Only categories with points earned appear in the chart. Tapping a segment navigates to a detail view for that category.

### Activity Calendar

A GitHub-style contribution heatmap showing your activity levels across the year. Each day is a small square, and the color intensity indicates how active you were. The current year is displayed in the header.

### Streak Counters

Two side-by-side cards:
- **Current Streak** — A flame icon with "X days" showing how many consecutive days you've completed at least one activity
- **Best Streak** — A trophy icon with "X days" showing your all-time longest streak

### Points Over Time

A full interactive points graph (same as the Home screen version) showing your cumulative points trend for the selected period. You can tap and drag to see values at specific dates.

---

## 10. The Profile Screen

The Profile screen (third tab) is where you manage your account, subscription, and app settings.

### Profile Header

A card showing:
- A circular avatar with your first initial on a gradient background
- Your full name (large, bold)
- Your email address
- A subscription badge (if active) showing the plan type, a star icon, and "X days left"
- Your join date

### Stats Summary

Three cards in a horizontal row:
- **Total Points** — Star icon, your lifetime total
- **Current Streak** — Flame icon, consecutive days
- **Best Streak** — Trophy icon, all-time record

### Account Section

- **Subscription** — Shows your current plan. Tapping opens the subscription management view where you can change plans, view renewal dates, or cancel.
- **Settings** — Opens the settings screen (see below).

### Support Section

- **Help & Support** — Opens help resources
- **Privacy Policy** — Opens the privacy policy
- **Terms of Service** — Opens the terms

### Sign Out

A red "Sign Out" button at the bottom. Tapping it shows a confirmation: "Are you sure you want to sign out?" with confirm and cancel options.

### Settings

The Settings screen has four sections:

**General**
- **Haptic Feedback** — Toggle on/off. Controls whether the app uses haptic vibrations for interactions.
- **Sound Effects** — Toggle on/off.
- **Notifications** — Toggle on/off. Controls reminders and completion alerts.
- **Motivational Quotes** — Toggle on/off.

**Display**
- **Appearance** — Choose between System (follows device), Light, or Dark mode. The current selection is marked with a checkmark.

**Data**
- **Export Data** — Export your activity data (placeholder for future implementation).
- **Clear Cache** — Clears locally cached data (destructive action, shown in red).

**About**
- **Version** — Shows the app version (1.0.0)
- **Developer Website** — Links to stng-studios.dk
- **Rate on App Store** — Links to the App Store listing

---

## 11. Design and Feel

### Visual Aesthetic

Neomi has a minimalist, premium feel. The design language is:

- **Typography**: SF Pro with clear hierarchy — large bold headings, medium subheadings, regular body text
- **Spacing**: Generous padding (16pt standard) and margins throughout. Nothing feels cramped.
- **Cards**: Subtle shadows, rounded corners (12pt radius standard, 8pt small, 16pt large). Cards sit on secondary backgrounds with clear elevation.
- **Icons**: SF Symbols throughout, consistent sizing and weight

### Color Themes

The app supports Light and Dark modes:

**Light Mode (Bone White)**
- Primary background: #F7F2EF (warm off-white)
- Card backgrounds: #FFFFFF (pure white)
- Nested sections: #E8E6E1 (light gray)
- Text: #1A1A1A (near-black primary), #666666 (secondary), #999999 (tertiary)
- Category colors are slightly muted (softer coral, sky blue, etc.)

**Dark Mode (Slate Blue)**
- Primary background: #1E293B (dark slate)
- Card backgrounds: #334155 (lighter slate)
- Nested sections: #475569 (even lighter slate)
- Text: #F8FAFC (near-white primary), #94A3B8 (secondary), #64748B (tertiary)
- Category colors are vibrant and saturated (bright coral, vivid blue, etc.)

The four category colors are consistent across both modes:
- **Physical**: Coral/Red tones
- **Mental**: Sky blue tones
- **Creative**: Purple tones
- **Everyday**: Teal tones

Each category has three shades: a base color, a lighter groove color (for card backgrounds), and an even lighter icon circle color. Text on category-colored backgrounds is always white.

### Animations

Animations are a key part of what makes Neomi feel satisfying:

- **Spring animations** (0.3 seconds) — Used for most transitions: tab switches, card expansions, button presses
- **Matched geometry effect** — The Add Habit grid-to-detail transition morphs the card smoothly into the configuration screen
- **Content transitions** — Numeric values (timers, points) animate with smooth number rolling
- **Scale and opacity** — Completion celebrations, button presses, and status changes use scale and fade effects
- **No spinners** — Loading states use skeleton screens instead of spinning indicators

### Haptic Feedback

The app uses iOS haptic feedback extensively to make interactions feel tactile:

- **Light impact** — Button taps, category tab selections, stepper changes, day-of-week toggles
- **Medium impact** — Activity completion, reaching timer target, completing an exercise set
- **Heavy impact** — Used sparingly for significant events
- **Success notification** — When finishing an activity and earning points
- **Warning notification** — When trying to start a second concurrent activity
- **Error notification** — When something goes wrong
- **Selection feedback** — Wheel and slider interactions
- **Custom patterns**:
  - **Points earned** — A continuous haptic with a smooth intensity curve (fades over 0.5 seconds)
  - **Task complete** — A three-pulse pattern with descending intensity (quick, satisfying triple-tap)

All haptics can be toggled off in Settings.

### Tab Bar

The bottom tab bar is a compact, centered pill shape — not a full-width bar. It has three icon-only tabs (Home, Stats, Profile) with a semi-transparent background. A sliding indicator shows the current tab with a glass-morphism effect. The tab bar subtly hides when you scroll down and reappears when you scroll up.

---

## 12. Offline and Sync

Neomi is designed to work completely offline. Your habits, todos, timers, and points all function without an internet connection.

### How It Works

- **Local-first**: All data is saved to your device first via local storage. The app is fully functional without connectivity.
- **Cloud sync**: When a connection is available, data syncs automatically to Supabase (the cloud backend). This happens when the app enters the background, when the network becomes available, and on a regular interval (every 5 minutes).
- **Conflict resolution**: If the same data was modified on multiple devices, the most recent change wins (last-write-wins).
- **Sync queue**: Changes made offline are queued and processed in order when connectivity returns. Failed syncs are retried up to 3 times with a 30-second delay between attempts.
- **Timer persistence**: If you close the app while a timer is running, the timer state is saved to device storage and restored when you reopen the app. If the timer's target was reached while the app was closed, it picks up seamlessly.

---

## 13. The Complete User Journey

Here's what a typical day looks like in Neomi:

1. **Open the app** — You see the Home screen with your points graph, daily progress ring (e.g., 0/5 completed), and your scheduled todos for today.

2. **Glance at your schedule** — Your todo list shows what's planned: maybe a 30-minute run, a 10-minute meditation, 20 minutes of reading, and 15 minutes of deep work.

3. **Start an activity** — Tap the "Start" button on your run todo. The screen fills with the Physical category's red color. A large timer ring appears and starts counting up.

4. **Work toward your target** — As you run, the progress ring fills. At 30 minutes, a haptic fires and "Target reached!" appears. But you're feeling good, so you keep going.

5. **Finish when ready** — At 35 minutes, you tap "Finish Run." The app records 35 minutes, calculates 21 points (35/10 x 6 = 21), and your todo updates to completed with a green checkmark.

6. **See your progress** — Back on the Home screen, your daily progress ring now shows 1/5 completed and "21 points today." The points graph updates with today's data.

7. **Continue through your day** — Start your meditation (a calm blue screen with breathing prompts), then your reading session (with book tracking), then your deep work (with a task checklist).

8. **Check your stats** — Tap the Stats tab to see your total points climbing, your streak extending, and your contribution calendar filling in.

9. **Day ends** — Any todos not completed by midnight are marked as missed. Tomorrow, your recurring habits will generate fresh todos automatically.

---

## 14. Upcoming Features

The following features are architecturally planned and structurally prepared in the codebase, but not yet active:

- **Focus Mode** — App-blocking during activities to prevent distraction
- **Social Features** — Friends, leaderboards, and shared challenges
- **Goals System** — Set weekly and monthly targets for points or activity counts
- **Apple Health Integration** — Sync activity data with Apple Health
- **Advanced Analytics** — Deeper insights into habits and patterns
- **Streak Bonuses** — Bonus points for maintaining long streaks (e.g., 50 bonus points for a perfect day)

---

## 15. Technical Summary

| Detail | Value |
|--------|-------|
| Platform | iOS 18.0+ (iPhone only) |
| Framework | SwiftUI |
| Backend | Supabase (PostgreSQL + Auth + Real-time) |
| Authentication | Apple Sign In |
| Offline Support | Full — local-first with cloud sync |
| Subscription | StoreKit 2 (monthly $4.99 / yearly $39.99) |
| Bundle ID | dk.stng-studios.Neomi |
| Developer | STNG Studios (Denmark) |

<div align="center">

# PyroMTProto

**Telegram MTProto API Library for Python**

Fast. Simple. Complete.

[![Layer](https://img.shields.io/badge/Telegram%20Layer-227-blue?style=flat-square)](https://core.telegram.org/schema)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?style=flat-square)](https://python.org)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange?style=flat-square)](https://pypi.org/project/pyromtproto)
[![License](https://img.shields.io/badge/License-LGPL--3.0-red?style=flat-square)](COPYING.lesser)

```bash
pip install pyromtproto
```

</div>

---

## What is PyroMTProto?

PyroMTProto is a Python library to interact with Telegram's MTProto API. It lets you build bots, automation tools, and user clients with full access to every Telegram feature.

```python
from pyrogram import Client

async with Client("my_account") as app:
    await app.send_message("me", "Hello!")
```

---

## Installation

```bash
pip install pyromtproto

# Faster crypto + event loop
pip install pyromtproto[fast]
```

**Requirements:** Python 3.10+

---

## Quick Example

```python
from pyrogram import Client, filters

app = Client("my_bot", api_id=12345, api_hash="abc...")

@app.on_message(filters.text)
async def echo(client, message):
    await message.reply(message.text)

app.run()
```

---

## Features

### 🚀 High Speed

- **Upload: 15–20 MB/s** — parallel multi-session upload with adaptive pool sizing
- **Download: 15–20 MB/s** — 4 parallel connections per data center
- Optimized TCP — low latency, large buffers, no fragmented reads

### 📡 Telegram Layer 227

Full support for the latest Telegram API — 2465 TL objects including all new types and functions.

### 💬 Messaging

```python
# Send text with formatting
await app.send_message(chat_id, "Hello **World**")

# Send photo with caption
await app.send_photo(chat_id, "photo.jpg", caption="My photo")

# Send video
await app.send_video(chat_id, "video.mp4")

# Send document
await app.send_document(chat_id, "file.pdf")

# Send voice / audio
await app.send_voice(chat_id, "voice.ogg")
await app.send_audio(chat_id, "song.mp3")

# Forward messages
await app.forward_messages(to_chat, from_chat, message_ids=[1, 2, 3])

# Pin a message
await app.pin_chat_message(chat_id, message_id)

# Delete messages
await app.delete_messages(chat_id, [msg_id_1, msg_id_2])
```

### 🎨 Rich Text Builder

Build formatted messages without writing HTML or Markdown:

```python
from pyrogram.types import RichText

msg = (
    RichText()
    .bold("Hello!\n")
    .italic("This is italic\n")
    .code("print('hello')")
    .newline()
    .link("Click here", "https://example.com")
    .newline()
    .spoiler("Hidden text")
    .newline()
    .blockquote("A quote", expandable=True)
    .newline()
    .diff_insert("Added line")
    .newline()
    .diff_delete("Removed line")
)

await app.send_message("me", **msg.to_message_kwargs())

# Works for media captions too
await app.send_photo("me", "photo.jpg", **msg.to_caption_kwargs())
```

**Available methods:**

| Method | Output |
|---|---|
| `.bold(text)` | **Bold** |
| `.italic(text)` | *Italic* |
| `.underline(text)` | Underline |
| `.strikethrough(text)` | ~~Strike~~ |
| `.spoiler(text)` | Spoiler |
| `.code(text)` | `Code` |
| `.pre(text, language="")` | Code block |
| `.blockquote(text, expandable=False)` | Blockquote |
| `.link(label, url)` | Hyperlink |
| `.mention(name, user_id)` | User mention |
| `.emoji(placeholder, document_id)` | Custom emoji |
| `.diff_insert(text)` | Green highlight |
| `.diff_delete(text)` | Red highlight |
| `.diff_replace(text)` | Yellow highlight |
| `.timestamp(text, unix_time)` | Local time |

### 🎨 Colour Buttons

```python
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

await app.send_message(
    chat_id,
    "Pick one:",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Yes", "yes", style=ButtonStyle.SUCCESS),
        InlineKeyboardButton("❌ No",  "no",  style=ButtonStyle.DANGER),
        InlineKeyboardButton("ℹ️ Info","info", style=ButtonStyle.PRIMARY),
    ]])
)
```

### 📋 Checklists

```python
# Send a checklist
await app.send_checklist(
    chat_id,
    title="Todo List",
    tasks=["Task 1", "Task 2", "Task 3"]
)

# Mark tasks as done
await app.mark_checklist_tasks_as_done(chat_id, message_id, task_ids=[1, 2])

# Edit checklist
await app.edit_message_checklist(chat_id, message_id, tasks=[...])
```

### 🏢 Business Accounts

```python
# Set your business intro
await app.update_business_intro(
    title="Welcome!",
    description="I reply within 2 hours."
)

# Set your location
await app.update_business_location(
    address="123 Main Street, Mumbai",
    latitude=19.0760,
    longitude=72.8777
)

# Set working hours
await app.update_business_work_hours(
    timezone="Asia/Kolkata",
    intervals=[...]
)

# Auto-reply when you are away
await app.update_business_away_message(
    shortcut_id=1,
    schedule="outside_work_hours",
    recipients_type="non_contacts"
)

# Greeting for first-time messagers
await app.update_business_greeting_message(
    shortcut_id=2,
    no_activity_days=7
)

# Business chat deep-links
link = await app.create_business_chat_link(
    text="Hi! I want to order.",
    title="Order Link"
)
print(link.link)  # https://t.me/m/xxxxxxxx

await app.get_business_chat_links()
await app.edit_business_chat_link("slug", title="New Title")
await app.delete_business_chat_link("slug")
await app.resolve_business_chat_link("slug")
```

### 🎁 Star Gifts

```python
# Send a gift
gifts = await app.get_available_gifts()
await app.send_gift(
    user_id="username",
    gift_id=gifts.gifts[0].id,
    text="Happy Birthday! 🎂"
)

# Browse gifts
async for gift in app.get_user_gifts("username"):
    print(gift.id, gift.stars)

# Manage received gifts
await app.save_gift("me", message_id=123)              # Show on profile
await app.save_gift("me", message_id=123, unsave=True) # Hide
await app.convert_gift("me", message_id=123)           # Convert to Stars
await app.upgrade_gift("me", message_id=123)           # Make it Unique
await app.transfer_gift(gift_id=456, to_user_id="friend")

# Preview upgrade
preview = await app.get_gift_upgrade_preview(gift_id=123)
```

### 🚀 Boosts & Giveaways

```python
# Channel boost info
status = await app.get_boost_status("@channel")
print(f"Level {status.level} — {status.boosts} boosts")

# See all boosters
async for boost in app.get_boosts_list("@channel"):
    print(boost.user_id)

# Boost a channel with your Premium slots
await app.apply_boost("@channel")

# Your boost status
my = await app.get_my_boosts()

# Specific user's boosts
await app.get_user_boosts("@channel", "username")
```

### 📖 Stories

```python
# Post a story
await app.post_story(chat_id, media="photo.jpg", caption="My story")

# React to a story
await app.send_story_reaction("username", story_id=5, reaction="❤️")

# See story viewers
async for viewer in app.get_story_viewers(story_id=5):
    print(viewer.user_id)

# See story reactions
async for r in app.get_story_reactions(story_id=5):
    print(r.peer_id)

# Stealth Mode — hide your views (Premium)
await app.activate_stealth_mode()

# Get a shareable link
link = await app.export_story_link("@channel", story_id=5)

# Register views
await app.increment_story_views("@channel", story_ids=[1, 2, 3])
```

### 📢 Suggested Posts

```python
# Approve a post submitted to your channel
await app.approve_suggested_post("@channel", message_id=42)

# Approve and schedule
from datetime import datetime, timezone, timedelta
await app.approve_suggested_post(
    "@channel",
    message_id=42,
    schedule_date=datetime.now(timezone.utc) + timedelta(hours=2)
)

# Decline with reason
await app.decline_suggested_post(
    "@channel",
    message_id=42,
    comment="Does not match our topic."
)

# Check status on a message
print(msg.suggested_post.is_pending)
print(msg.suggested_post.accepted)
print(msg.suggested_post.schedule_date)
```

### 📸 Cover Photo

```python
# Set a channel cover (banner image, separate from avatar)
await app.set_chat_photo("@channel", cover="banner.jpg")

# Set avatar + cover together
await app.set_chat_photo("@channel", photo="avatar.jpg", cover="banner.jpg")
```

### 🤖 AI Compose Tones

```python
# List all tones
tones = await app.get_ai_compose_tones()

# Get a tone
await app.get_ai_compose_tone("formal")

# See a rewrite example
example = await app.get_ai_compose_tone_example("casual")

# Create a custom tone (Premium)
await app.create_ai_compose_tone(
    title="My Tone",
    prompt="Rewrite in a friendly style."
)

# Manage tones
await app.update_ai_compose_tone(tone_id=123, title="New Name")
await app.save_ai_compose_tone("formal")
await app.delete_ai_compose_tone(tone_id=123)
```

### 🗂️ Forum Topics

```python
await app.create_forum_topic(chat_id, "General", icon_color=0x6FB9F0)
await app.edit_forum_topic(chat_id, topic_id, name="New Name")
await app.close_forum_topic(chat_id, topic_id)
await app.reopen_forum_topic(chat_id, topic_id)
await app.delete_forum_topic(chat_id, topic_id)
await app.hide_forum_topic(chat_id, topic_id)
await app.unhide_forum_topic(chat_id, topic_id)
await app.toggle_forum_topic_is_pinned(chat_id, topic_id, is_pinned=True)
await app.get_forum_topics(chat_id)
await app.get_forum_topic(chat_id, topic_id)
await app.get_forum_topic_icon_stickers()
```

### 👥 Users & Chats

```python
# Get user/chat info
user = await app.get_users("username")
chat = await app.get_chat("@channel")

# Get members
async for member in app.get_chat_members(chat_id):
    print(member.user.first_name)

# Ban / unban
await app.ban_chat_member(chat_id, user_id)
await app.unban_chat_member(chat_id, user_id)

# Promote / restrict
await app.promote_chat_member(chat_id, user_id, ...)
await app.restrict_chat_member(chat_id, user_id, ...)

# Set title / description / photo
await app.set_chat_title(chat_id, "New Title")
await app.set_chat_description(chat_id, "About us")
await app.set_chat_photo(chat_id, photo="photo.jpg")
```

### 🤖 Bots & Inline

```python
# Answer inline queries
@app.on_inline_query()
async def answer(client, query):
    await query.answer([
        InlineQueryResultArticle(
            title="Hello",
            input_message_content=InputTextMessageContent("Hello!")
        )
    ])

# Answer callback queries
@app.on_callback_query()
async def callback(client, query):
    await query.answer("Button clicked!")

# Send invoice
await app.send_invoice(chat_id, title="Product", ...)
```

### 📊 Polls

```python
# Send a poll
await app.send_poll(
    chat_id,
    question="Favourite language?",
    options=["Python", "JavaScript", "Rust"],
    is_anonymous=True
)

# Quiz mode
await app.send_poll(
    chat_id,
    question="Capital of France?",
    options=["London", "Paris", "Berlin"],
    type="quiz",
    correct_option_id=1
)
```

### 📞 Phone / Contacts

```python
# Get contacts
contacts = await app.get_contacts()

# Add contact
await app.add_contact(user_id, first_name="John")

# Delete contact
await app.delete_contacts([user_id])

# Block / unblock
await app.block_user(user_id)
await app.unblock_user(user_id)
```

### 🔗 Invite Links

```python
# Create invite link
link = await app.create_chat_invite_link(
    chat_id,
    name="My Link",
    member_limit=100,
    expire_date=datetime.now() + timedelta(days=7)
)

# Revoke a link
await app.revoke_chat_invite_link(chat_id, link.invite_link)

# Get pending join requests
async for req in app.get_chat_join_requests(chat_id):
    await app.approve_chat_join_request(chat_id, req.from_user.id)
```

### 🔍 Search

```python
# Search messages
async for msg in app.search_messages(chat_id, query="hello"):
    print(msg.text)

# Search globally
async for msg in app.search_global("python"):
    print(msg.chat.title, msg.text)

# Get message history
async for msg in app.get_chat_history(chat_id, limit=100):
    print(msg.text)
```

### 🌐 Raw API Access

Full access to every Telegram API function:

```python
from pyrogram import raw

# Call any raw TL function
result = await app.invoke(
    raw.functions.messages.GetHistory(
        peer=await app.resolve_peer("username"),
        offset_id=0,
        offset_date=0,
        add_offset=0,
        limit=10,
        max_id=0,
        min_id=0,
        hash=0
    )
)

# Access all Layer 227 types
from pyrogram.raw.types import SuggestedPost, KeyboardButtonStyle
from pyrogram.raw.functions.aicompose import GetTones
```

---

## Filters & Handlers

```python
from pyrogram import filters

# Text messages
@app.on_message(filters.text)
async def on_text(client, msg): ...

# Commands
@app.on_message(filters.command("start"))
async def on_start(client, msg): ...

# Photos
@app.on_message(filters.photo)
async def on_photo(client, msg): ...

# Private chats only
@app.on_message(filters.private & filters.text)
async def on_private(client, msg): ...

# Specific chat
@app.on_message(filters.chat("@mychannel"))
async def on_channel(client, msg): ...

# Edited messages
@app.on_edited_message(filters.text)
async def on_edit(client, msg): ...

# Callback queries
@app.on_callback_query()
async def on_button(client, query): ...
```

---

## Stats

| | |
|---|---|
| Telegram Layer | **227** |
| TL Objects | **2465** |
| Python | **3.10+** |
| Upload Speed | **15–20 MB/s** |
| Download Speed | **15–20 MB/s** |

---

## License

LGPL-3.0 — see [COPYING.lesser](COPYING.lesser)

# Capstone Project

## Project Aim
This project aims to develop a cross-platform analytics system that compares the social media engagement of brands and events across YouTube, Instagram, and X. It will collect publicly available engagement metrics, such as views, likes, comments, and shares, and present the results through an interactive dashboard to support more meaningful comparisons between platforms.

## Platforms
- YouTube
- Instagram
- X

## Data to Collect
- Views
- Likes
- Comments
- Shares, when available
- Publication date

## Planned Output
A dashboard and analysis comparing engagement across the three platforms.

## Post Data Format

Sample data is stored in `data/raw/sample_posts.csv`.

- Each row represents one social media post.
- `entity_name` identifies the brand or event.
- `platform` identifies the social media platform.
- `post_url` links to the original post.
- `published_at` records the publication date.
- `collected_at` records when the metrics were observed.
- `views`, `likes`, `comments`, and `shares` contain engagement counts.
- Blank metrics mean unavailable, not zero.

The first sample was collected manually from YouTube.
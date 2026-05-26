from flask import Flask, render_template

app = Flask(__name__)

# ── Main pages ───────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('base.html', page='home')

@app.route('/about')
def about():
    return render_template('base.html', page='about')

@app.route('/programs')
def programs():
    return render_template('base.html', page='programs')

@app.route('/events')
def events():
    return render_template('base.html', page='events')

@app.route('/donate')
def donate():
    return render_template('base.html', page='donate')

@app.route('/volunteer')
def volunteer():
    return render_template('base.html', page='volunteer')

@app.route('/contact')
def contact():
    return render_template('base.html', page='contact')

# ── Past event detail pages ──────────────────────────────────
EVENTS = {
    'kids-market': {
        'title': 'Kids Market at St. Charles',
        'date': 'May 3, 2026',
        'category': 'Community Initiative',
        'cover_image': '/static/images/kids_market_1.png',
        'description': (
            'Heartfelt appreciation to everyone who took part in this month\'s Sai Palkhi event, '
            'where we tried something new and exciting by involving kids in running a business at '
            'the St. Charles market. The experience was truly enriching for the youth volunteers '
            'who learned about the end-to-end process — from setting up the stall, answering '
            'customers\' queries, to selling and managing the POS. A huge thanks to all the '
            'parents and volunteers who made this possible.'
        ),
        'link': None,
        'link_text': None,
        'gallery': [
            '/static/images/kids_market_2.png',
            '/static/images/kids_market_3.png',
        ]
    },
    'book-drive': {
        'title': 'Book Drive with Ready Readers',
        'date': 'April 19, 2026',
        'category': 'Educational Initiative',
        'cover_image': '/static/images/book_drive_cover.png',
        'description': (
            'Our heartfelt thanks to each and every one of the youth volunteers who participated '
            'in our book drive. From the kind donors to the tireless volunteers and the kids who '
            'pitched in to help sort and organize the boxes, every single one of them played a '
            'vital role in making this initiative a success. We\'re thrilled to have collected '
            'around 400 books for the "Ready Readers" organization, which will be a valuable '
            'resource for many families in need. We\'re also looking forward to the opportunity '
            'to work with the organization again in the future, thanks to the director\'s '
            'gracious invitation.'
        ),
        'link': 'https://readyreaders.org/',
        'link_text': 'Learn more about Ready Readers',
        'gallery': [
            '/static/images/book_drive_1.png',
            '/static/images/book_drive_2.png',
            '/static/images/book_drive_3.png',
        ]
    },
    'palki-interfaith': {
        'title': 'Palki Gathering with Interfaith Team',
        'date': 'March 21, 2026',
        'category': 'Community Gathering',
        'cover_image': '/static/images/palki_interfaith_1.png',
        'description': (
            'We\'re grateful for community members\' presence at our Palki gathering, which made '
            'the evening truly special. Their participation enriched our discussion of the Guru '
            'Bhagwat\'s Volume 1 key messages and their deeper significance. Thank you all for '
            'your gracious presence.'
        ),
        'link': None,
        'link_text': None,
        'gallery': [
            '/static/images/palki_interfaith_2.png',
        ]
    },
    'blessings-box': {
        'title': 'Blessings in a Box',
        'date': 'March 8, 2026',
        'category': 'Community Service',
        'cover_image': '/static/images/blessings_box_1.png',
        'description': (
            'Our Blessings in a Box drive was truly heartwarming, thanks to the incredible '
            'enthusiasm of our young volunteers. A sincere thank you to all the parents for '
            'their support and generosity in bringing the supplies, encouraging the children, '
            'and helping make this initiative possible. Their involvement turned the event into '
            'a meaningful family and community effort. Together, we created something beautiful '
            '— an act of kindness that touched many lives, complete with live music. '
            'We\'re truly grateful to everyone who contributed to making this service project '
            'a resounding success.'
        ),
        'link': None,
        'link_text': None,
        'gallery': [
            '/static/images/blessings_box_2.png',
        ]
    },
    'food-drive': {
        'title': 'Food Drive for Homeless Shelter',
        'date': 'December 30, 2025',
        'category': 'Humanitarian Initiative',
        'cover_image': '/static/images/food_drive_1.png',
        'description': (
            'Volunteers came together during the holiday season to collect and distribute food '
            'to those in need at local homeless shelters. This drive reflected the foundation\'s '
            'core commitment to humanitarian service — ensuring that every community member has '
            'access to basic necessities and feels seen and supported.'
        ),
        'link': None,
        'link_text': None,
        'gallery': []
    },
}

@app.route('/event/<slug>')
def event_detail(slug):
    event = EVENTS.get(slug)
    if not event:
        return render_template('base.html', page='events')
    return render_template('base.html', page='event_detail', event=event)


if __name__ == '__main__':
    app.run(debug=True)
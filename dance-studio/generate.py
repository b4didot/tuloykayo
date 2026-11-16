from pathlib import Path
from html import escape

out = Path(__file__).parent / 'dist'
policies = ['Students must check in before entering their class.', 'Parents must pick up their children on time.', 'Students should notify the studio if they will be absent.', 'Missed classes are not automatically refunded.', 'Food is not allowed inside dance rooms.', 'Water bottles are allowed inside dance rooms.', 'Parents may observe classes from the designated viewing area.', 'Students must follow instructor directions during class.', 'Students should arrive 10 minutes before their scheduled class.']
trial = ['New students are eligible for one free trial class.', 'Trial classes must be scheduled 24 hours in advance.', 'Students should wear comfortable clothing for their trial class.']
other = ['The studio hosts one annual dance recital.', 'Recital participation is optional.', 'Recital costumes are purchased separately.', 'Students should bring their own water bottles.', 'The studio offers classes throughout the year.']
ages = ['The studio accepts students ages 3 to 18.', 'Ballet classes are available for ages 3 to 18.', 'Jazz classes are available for ages 6 to 18.', 'Hip-hop classes are available for ages 6 to 18.', 'Contemporary classes are available for ages 8 to 18.', 'Beginner classes do not require previous dance experience.', 'Advanced classes require instructor approval.', 'Students may enroll in more than one dance style.', 'All programs are open to boys and girls.']
schedule = ['The studio is open Monday through Friday, 9:00 AM to 8:00 PM.', 'Saturday classes are available from 9:00 AM to 3:00 PM.', 'The studio is closed on Sundays.', 'Each regular dance class lasts 60 minutes.', 'Ballet classes are held every Monday and Wednesday from 4:00 PM to 5:00 PM.', 'Jazz classes are held every Friday from 4:00 PM to 5:00 PM.', 'Hip-hop classes are held every Tuesday and Thursday from 5:00 PM to 6:00 PM.', 'Contemporary classes are held every Saturday from 10:00 AM to 11:00 AM.']
pricing = ['Ballet classes cost $200 per month.', 'Jazz classes cost $180 per month.', 'Hip-hop classes cost $150 per month.', 'Contemporary classes cost $190 per month.', 'Tuition is due on the first day of each month.', 'Dance uniforms and shoes are not included in tuition.', 'Recital costumes are charged separately at $100 per student.', 'Payments can be made by credit card or bank transfer.']
dress = ['Ballet students must wear a leotard, tights, and ballet shoes.', 'Jazz students must wear fitted dancewear and jazz shoes.']
locations = ['The studio is located at 123 Main Street, Springfield.', 'Free parking is available in front of the studio.', 'Parents may use the designated drop-off area near the entrance.', 'Office Address is 123 Main Street, Springfield.']

def section(title, facts, ident):
    return f'<section class="info" id="{ident}"><h2>{title}</h2><div>' + ''.join(f'<p>{escape(f)}</p>' for f in facts) + '</div></section>'

def page(name, title, subtitle, content):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if label == name else '')+f'>{label}</a>' for label,url in [('Home','index.html'),('Programs','programs.html'),('Contact Us','contact.html')])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{name} | Tuloy Dance Studio</title><meta name="description" content="Tuloy Dance Studio sample website. Dance programs, schedules, tuition, and studio information."><link rel="stylesheet" href="styles.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html"><span class="mark">t.</span><span>TULOY<small>DANCE STUDIO</small></span></a><nav aria-label="Main navigation">{nav}</nav><a class="header-cta" href="contact.html#visit">Visit the studio <span>↗</span></a></header>
<main id="main"><div class="page-intro"><p class="eyebrow">SPRINGFIELD · AGES 3–18</p><h1>{title}</h1><p class="subtitle">{subtitle}</p></div>{content}</main>
<footer><a class="brand" href="index.html">TULOY <small>DANCE STUDIO</small></a><p>123 Main Street, Springfield</p><p class="demo">Sample studio website · Scraper testing MVP</p></footer></body></html>'''

home = '''<section class="hero-art" aria-label="Dance is for everyone"><div class="orbit one"></div><div class="orbit two"></div><span class="art-label">A LITTLE COURAGE.<br>A LOT OF MOVEMENT.</span><div class="art-type">Find your<br><em>rhythm.</em></div><div class="art-bottom"><span>MOVE. LEARN. BELONG.</span><span>01 / TULOY</span></div></section><section class="welcome"><p class="eyebrow">ROOM TO GROW</p><h2>Small steps.<br>Big possibilities.</h2><div><p>From a first ballet step to a new hip-hop routine, there’s a place for every young dancer here.</p><p>Explore ballet, jazz, hip-hop, and contemporary classes throughout the year.</p><a class="button" href="programs.html">Explore our programs ↗</a></div></section>'''
home += section('Your first class is on us', trial, 'trial-policy')
home += section('General policies', policies, 'general-policies')
home += section('Beyond the classroom', other, 'other')
home += '<aside class="reference-note"><h2>What families can be told today</h2><p>Reference screenshot note: 10 FAQs · 2 documents are counted separately under Knowledge sources above; Ready facts only counts approved fact answers.</p></aside>'
cards = '<div class="program-grid">'
for num,style,age,price,days in [('01','Ballet','3–18','$200','Monday & Wednesday · 4–5 PM'),('02','Jazz','6–18','$180','Friday · 4–5 PM'),('03','Hip-hop','6–18','$150','Tuesday & Thursday · 5–6 PM'),('04','Contemporary','8–18','$190','Saturday · 10–11 AM')]:
    cards += f'<article class="program"><span class="program-number">{num} / DANCE</span><h2>{style}</h2><p>Ages {age}</p><p>{days}</p><div class="price">{price}<small> / month</small></div></article>'
cards += '</div>'
programs = cards + section('Programs & ages', ages, 'programs-ages') + section('Schedule', schedule, 'schedule') + section('Pricing', pricing, 'pricing') + section('Dress code', dress, 'dress-code')
contact = '<section class="visit" id="visit"><div><p class="eyebrow">COME SAY HELLO</p><h2>See you at<br>the studio.</h2><address>123 Main Street<br>Springfield</address><p>Stop by during studio hours to ask about our programs or schedule your free trial class.</p><a class="text-link" href="programs.html#schedule">View class schedule ↗</a></div><div class="address-art"><span class="pin">●</span><span>123<br><small>MAIN STREET</small></span><p>SPRINGFIELD</p></div></section>' + section('Locations', locations, 'locations') + section('Studio hours', schedule[:3], 'hours') + section('Plan your trial', trial, 'trial-policy')
for file,name,title,subtitle,body in [('index.html','Home','Every dancer starts<br>with a <em>first step.</em>','A welcoming place for young dancers to move, discover, and grow.',home),('programs.html','Programs','Find your kind<br>of <em>movement.</em>','Four dance styles. A world of possibility. Explore your next step.',programs),('contact.html','Contact Us','Let’s get<br><em>moving.</em>','Visit our Springfield studio and start your dance journey.',contact)]:
    (out/file).write_text(page(name,title,subtitle,body),encoding='utf-8')
print('Generated 3 static pages; all 48 supplied studio facts included.')

import json

# Define the list of first aid items
first_aid_items = [
    {"title": "Skin Cut", "description": "Learn how to treat a minor skin cut.", "video_url": "https://www.youtube.com/embed/AhANvBB9hz0", "image_url": "https://clipground.com/images/skin-cut-clipart.jpg", "keywords": "skin cut wound"},
    {"title": "Burns", "description": "Learn how to treat burns.", "video_url": "https://www.youtube.com/embed/IKwD91qmXDo", "image_url": "https://raisingchildren.net.au/__data/assets/image/0016/47041/Burns-and-scalds-what-to-do-PIP-1.gif", "keywords": "burn treatment"},
    {"title": "Snake Bite", "description": "Steps to treat a snake bite.", "video_url": "https://www.youtube.com/embed/JUsneRS8_zA", "image_url": "https://www.shutterstock.com/image-vector/snake-bite-first-aid-medical-260nw-2300423579.jpg", "keywords": "snake bite"},
    {"title": "Heart Attack", "description": "What to do if someone has a heart attack.", "video_url": "https://www.youtube.com/embed/qvf_74DM880", "image_url": "https://th.bing.com/th/id/R.17d8e11685c8683a6b31b5582ad45a82?rik=TsYbcTUiCpEsFw&riu=http%3a%2f%2fmedlarge.com%2fwp-content%2fuploads%2f2018%2f02%2flearn-key-differences-among-cardiac-arrest-heart-attack-stroke-1024x538.jpg&ehk=BmR8JrZlw5NppfzIl837G8KQyONmMD7ZUuQt0mB5PdQ%3d&risl=&pid=ImgRaw&r=0", "keywords": "heart attack first aid"},
    {"title": "Severe Bleeding", "description": "How to control severe bleeding.", "video_url": "https://www.youtube.com/embed/8pTaqY40-Rs", "image_url": "https://www.baptisthealthsystem.com/images/global/newsroom-ccb/infographics/when-does-bleeding-need-emergency-care/bleeding-er-care-02.jpg", "keywords": "severe bleeding wound"},
    {"title": "Choking", "description": "How to perform the Heimlich maneuver on someone choking.", "video_url": "https://www.youtube.com/embed/nfHGzD93XuU", "image_url": "https://as2.ftcdn.net/jpg/00/69/32/89/500_F_69328956_P677Q2xLquvWlwE8C2g8DmIlZnWcwSNB.jpg", "keywords": "choking Heimlich maneuver"},
    {"title": "Fracture", "description": "How to treat a fracture until medical help arrives.", "video_url": "https://www.youtube.com/embed/2v8vlXgGXwE", "image_url": "https://thumbs.dreamstime.com/b/fracture-man-vector-fracture-man-vector-injury-pain-treatment-healthcare-physical-arthritis-care-trauma-body-fracture-man-272279238.jpg", "keywords": "fracture injury first aid"},
    {"title": "Asthma Attack", "description": "What to do if someone has an asthma attack.", "video_url": "http://www.youtube.com/embed/A3Z_J-Rn_ew", "image_url": "https://static.vecteezy.com/system/resources/previews/012/678/324/non_2x/man-uses-an-asthma-inhaler-against-attack-world-asthma-day-allergy-bronchial-asthma-illustration-vector.jpg", "keywords": "asthma attack first aid"},
    {"title": "Heatstroke", "description": "How to treat heatstroke and prevent further complications.", "video_url": "https://www.youtube.com/embed/jvGC_dQJUtE", "image_url": "https://th.bing.com/th/id/OIP.AxDao2CGWbxJ7sxvYS_S7AHaHa?rs=1&pid=ImgDetMain", "keywords": "heatstroke first aid"},
    {"title": "Hypothermia", "description": "How to handle hypothermia.", "video_url": "https://www.youtube.com/embed/dEKaCOx7igI", "image_url": "https://www.verywellhealth.com/thmb/nW6TG8apu44SuGnWPpV7gvCeZHo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hypothermia-overview-4161047_final-58e7d68033884440ba6b407fab0e2277.png", "keywords": "hypothermia treatment"},
    {"title": "Electric Shock", "description": "Steps to take when someone experiences an electric shock.", "video_url": "https://www.youtube.com/embed/gOOpGOoAGD4", "image_url": "https://th.bing.com/th/id/OIP.juuXn5hFfD6BABKQVPe2AgHaHa?rs=1&pid=ImgDetMain", "keywords": "electric shock first aid"},
    {"title": "Poisoning", "description": "What to do if someone is poisoned.", "video_url": "https://www.youtube.com/embed/b2ieb8BZJuY", "image_url": "https://acko-cms.ackoassets.com/First_Aid_Guide_Dealing_with_a_case_of_poisoning_8c28775984.png", "keywords": "poisoning first aid"},
    {"title": "Severe Allergic Reaction", "description": "How to treat someone having an allergic reaction.", "video_url": "https://www.youtube.com/embed/0Q5npXJ8KUY", "image_url": "https://png.pngtree.com/png-vector/20221022/ourlarge/pngtree-set-of-allergy-symptoms-cartoon-vector-illustration-png-image_6338109.png", "keywords": "allergic reaction first aid"},
    {"title": "Drowning", "description": "First aid for someone who has drowned.", "video_url": "https://www.youtube.com/embed/0lDl-vpKXF4", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtC5BK7T3ZycaYurxqomJREJIP5oV_FUVLkA&s", "keywords": "drowning first aid"}
]

# data.py

hospitals= [
        {
            "name": "Apollo Hospitals",
            "address": "Jubilee Hills, Hyderabad",
            "phone": "+91 40 2360 7777",
            "map_link": "https://maps.google.com/?q=Apollo+Hospitals+JubileeHills"
        },
        {
            "name": "Care Hospitals",
            "address": "Banjara Hills, Hyderabad",
            "phone": "+91 40 3041 7777",
            "map_link": "https://maps.google.com/?q=Care+Hospitals+BanjaraHills"
        },
        {
            "name": "Yashoda Hospitals",
            "address": "Malakpet, Hyderabad",
            "phone": "+91 40 4567 4567",
            "map_link": "https://maps.google.com/?q=Yashoda+Hospitals+Malakpet"
        },
        {
            "name": "Supraja Hospitals",
            "address": "Nagole, Hyderabad",
            "phone": "+91 40 2980 2345",
            "map_link": "https://maps.google.com/?q=Supraja+Hospital+Nagole"
        },
        {
            "name": "Sri Harsha Hospitals",
            "address": "Anandnagar, Hyderabad",
            "phone": "+91 4029329999",
            "map_link": "https://maps.google.com/?q=Sri+Harsha+Hospitals+Anandnagar"
        },
        {
            "name": "Srinivasa Hospital",
            "address": "LB Nagar, Hyderabad",
            "phone": "+91 40 2403 5678",
            "map_link": "https://maps.google.com/?q=Srinivasa+Hospital+LB+Nagar"
        },
        {
            "name": "Zoi Hospitals",
            "address": "Attapur, Hyderabad (Nearby Anandnagar)",
            "phone": "+91 40 4850 5050",
            "map_link": "https://maps.google.com/?q=Zoi+Hospitals+Attapur"
        },
        {
            "name": "Owaisi Hospital & Research Centre",
            "address": "Kanchanbagh, Near Balapur, Hyderabad",
            "phone": "+91 40 2434 3737",
            "map_link": "https://maps.google.com/?q=Owaisi+Hospital+Hyderabad"
        },
        {
            "name": "Om Sai Hospital",
            "address": "Balapur X Roads, Hyderabad",
            "phone": "+91 40 2453 1111",
            "map_link": "https://maps.google.com/?q=Om+Sai+Hospital+Balapur"
        },
        {
            "name": "Ayu Plus Hospital",
            "address": "Mamata Nagar Colony, Nagole, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Ayu+Plus+Hospital+Nagole+Hyderabad"
        },
        {
            "name": "SLMS Hospital",
            "address": "Nagole X Roads, Nagole, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=SLMS+Hospital+Nagole+Hyderabad"
        },
        {
            "name": "Bhavya Multi Speciality Hospital",
            "address": "Flag Apartment, Nagole, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Bhavya+Multi+Speciality+Hospital+Nagole+Hyderabad"
        },
        {
            "name": "Aparna Maternity & General Hospital",
            "address": "Beside SBH Bank, Bundlaguda Road, Nagole, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Aparna+Maternity+General+Hospital+Nagole+Hyderabad"
        },
        {
            "name": "Kamineni Hospitals",
            "address": "L.B. Nagar, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Kamineni+Hospitals+LB+Nagar+Hyderabad"
        },
        {
            "name": "Aware Gleneagles Global Hospitals",
            "address": "Sagar Road, L.B. Nagar, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Aware+Gleneagles+Global+Hospitals+LB+Nagar+Hyderabad"
        },
        {
            "name": "Rainbow Children's Hospital",
            "address": "Mansoorabad Village, L.B. Nagar, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Rainbow+Children's+Hospital+LB+Nagar+Hyderabad"
        },
        {
            "name": "Raksha Multi Speciality Hospital",
            "address": "Chintalkunta Checkpost, L.B. Nagar, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Raksha+Multi+Speciality+Hospital+LB+Nagar+Hyderabad"
        },
        {
            "name": "Yashoda Hospital",
            "address": "Nalgonda X Roads, Malakpet, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Yashoda+Hospital+Malakpet+Hyderabad"
        },
        {
            "name": "Metro Cure Hospitals",
            "address": "Judges Colony, Old Malakpet, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Metro+Cure+Hospitals+Malakpet+Hyderabad"
        },
        {
            "name": "Imtiyaz Hospital",
            "address": "Akbar Towers, Malakpet, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Imtiyaz+Hospital+Malakpet+Hyderabad"
        },
        {
            "name": "Meta Nova Ayurveda and Panchakarma Center",
            "address": "Triveni Nagar, Balapur X Road, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Meta+Nova+Ayurveda+and+Panchakarma+Center+Balapur+Hyderabad"
        },
        {
            "name": "Shri Anish Clinic",
            "address": "Triveni Nagar, Balapur X Road, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Shri+Anish+Clinic+Balapur+Hyderabad"
        },
        {
            "name": "Sree Nayanam Eye Clinic",
            "address": "Akshara School Building, Bheeshma Nagar, Badangpet, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Sree+Nayanam+Eye+Clinic+Balapur+Hyderabad"
        },
        {
            "name": "Aruna Hospital",
            "address": "Chandrapur Colony, L.B. Nagar, Hyderabad",
            "phone": "Not specified",
            "map_link": "https://maps.google.com/?q=Aruna+Hospital+LB+Nagar+Hyderabad"
        }
            # Add more hospital dictionaries here...
    ]

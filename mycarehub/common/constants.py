WHITELIST_COUNTIES = [
    "Kajiado",
    "Nairobi",
]


_CONSTITUENCIES = "Constituencies"
_SUB_COUNTIES = "Sub Counties"
ADMINISTRATIVE_UNITS = {
    "Nairobi": {
        _CONSTITUENCIES: (
            "Dagoretti North",
            "Dagoretti South",
            "Embakasi Central",
            "Embakasi East",
            "Embakasi North",
            "Embakasi South",
            "Embakasi West",
            "Kamukunji",
            "Kasarani",
            "Kibra",
            "Langata",
            "Makadara",
            "Mathare",
            "Roysambu",
            "Ruaraka",
            "Starehe",
            "Westlands",
        ),
        _SUB_COUNTIES: {
            "Dagoretti North": ("Gatini", "Kabiro", "Kawangware", "Kileleshwa", "Kilimani"),
            "Dagoretti South": ("Mutu-Ini", "Ngando", "Riruta", "Uthiru/Ruthimitu", "Waithaka"),
            "Embakasi Central": (
                "Kayole Central",
                "Kayole North",
                "Kayole South",
                "Komarock",
                "Matopeni/Spring Valley",
            ),
            "Embakasi East": (
                "Embakasi",
                "Lower Savannah",
                "Mihango",
                "Upper Savannah",
                "Utawala",
            ),
            "Embakasi North": (
                "Dandora Area I",
                "Dandora Area II",
                "Dandora Area III",
                "Dandora Area Iv",
                "Karioboangi North",
            ),
            "Embakasi South": ("Imara Daima", "Kwa Njenga", "Kwa Rueben", "Kware", "Pipeline"),
            "Embakasi West": (
                "Kariobangi South",
                "Maringo/Hamza",
                "Mowlem",
                "Umoja I",
                "Umoja II",
            ),
            "Kamukunji": (
                "Airbase",
                "California",
                "Eastleigh North",
                "Eastleigh South",
                "Pumwani",
            ),
            "Kasarani": ("Clay City", "Kasarani", "Mwiki", "Njiru", "Ruai"),
            "Kibra": (
                "Laini Saba",
                "Lindi",
                "Makina" "Sarang'ombe",
                "Woodley/Kenyatta Golf Course",
            ),
            "Langata": ("Karen", "Mugumo-ini", "Nairobi West", "Nyayo Highrise", "South C"),
            "Makadara": ("Harambee", "Makongeni", "Maringo/Hamza", "Viwandani"),
            "Mathare": ("Hospital", "Huruma", "Kiamaiko", "Mabatini", "Ngei"),
            "Roysambu": ("Githurai", "Kahawa", "Kahawa West", "Roysambu", "Zimmerman"),
            "Ruaraka": ("Babandogo", "Korogocho", "Lucky Summer", "Mathare North", "Utalii"),
            "Starehe": (
                "Landimawe",
                "Nairobi Central",
                "Nairobi South",
                "Ngara",
                "Pangani",
                "Ziwani/Kariokor",
            ),
            "Westlands": ("Kangemi", "Karura", "Kitisuru", "Mountain View", "Parklands/Highridge"),
        },
    },
    "Kajiado": {
        _CONSTITUENCIES: (
            "Kajiado Central",
            "Kajiado East",
            "Kajiado North",
            "Kajiado West",
            "Magadi",
        ),
        _SUB_COUNTIES: {
            "Kajiado Central": (
                "Dalalekutuk",
                "Ildamat",
                "Matapato North",
                "Matapato South",
                "Purko",
            ),
            "Kajiado East": (
                "Imaroro",
                "Kaputiei North",
                "Kenyawa-poka",
                "Kitengela",
                "Oloosirkon/Sholinke",
            ),
            "Kajiado North": ("Ngong", "Nkaimurunya", "Olkeri", "Oloolua", "Ongata Rongai"),
            "Kajiado West": (
                "Ewuaso Oo Nkidong'i",
                "Iloodokilani",
                "Keekonyokie",
                "Magadi",
                "Mosiro",
            ),
            "Loitokitok": (
                "Entonet/Lenkism",
                "Imbrikani/Eselelnkei",
                "Kimana",
                "Kuku",
                "Rombo",
            ),
        },
    },
    "Kirinyaga": {
        _CONSTITUENCIES: (
            "Kirinyaga Central",
            "Kirinyaga East",
            "Kirinyaga West",
        ),
        _SUB_COUNTIES: {
            "Kirinyaga Central": (),
            "Kirinyaga East": (),
            "Kirinyaga West": (),
        },
    },
    "Kiambu": {
        _CONSTITUENCIES: (
            "Kiambu Township",
            "Githunguri",
            "Kiambaa",
            "Lari",
            "Limuru",
            "Kabete",
            "Thika Town",
            "Juja",
            "Gatundu South",
            "Gatundu North",
            "Ruiru",
        ),
        _SUB_COUNTIES: {
            "Kiambu Township": (),
            "Githunguri": (),
            "Kiambaa": (),
            "Lari": (),
            "Limuru": (),
            "Kabete": (),
            "Thika Town": (),
            "Juja": (),
            "Gatundu South": (),
            "Gatundu North": (),
            "Ruiru": (),
        },
    },
}

COUNTRY_CODES = (
    ("ABW", "Aruba"),
    ("AFG", "Afghanistan"),
    ("AGO", "Angola"),
    ("AIA", "Anguilla"),
    ("ALA", "\u00c5land Islands"),
    ("ALB", "Albania"),
    ("AND", "Andorra"),
    ("ARE", "United Arab Emirates"),
    ("ARG", "Argentina"),
    ("ARM", "Armenia"),
    ("ASM", "American Samoa"),
    ("ATA", "Antarctica"),
    ("ATF", "French Southern Territories"),
    ("ATG", "Antigua and Barbuda"),
    ("AUS", "Australia"),
    ("AUT", "Austria"),
    ("AZE", "Azerbaijan"),
    ("BDI", "Burundi"),
    ("BEL", "Belgium"),
    ("BEN", "Benin"),
    ("BES", "Bonaire, Sint Eustatius and Saba"),
    ("BFA", "Burkina Faso"),
    ("BGD", "Bangladesh"),
    ("BGR", "Bulgaria"),
    ("BHR", "Bahrain"),
    ("BHS", "Bahamas"),
    ("BIH", "Bosnia and Herzegovina"),
    ("BLM", "Saint Barth\u00e9lemy"),
    ("BLR", "Belarus"),
    ("BLZ", "Belize"),
    ("BMU", "Bermuda"),
    ("BOL", "Bolivia (Plurinational State of)"),
    ("BRA", "Brazil"),
    ("BRB", "Barbados"),
    ("BRN", "Brunei Darussalam"),
    ("BTN", "Bhutan"),
    ("BVT", "Bouvet Island"),
    ("BWA", "Botswana"),
    ("CAF", "Central African Republic"),
    ("CAN", "Canada"),
    ("CCK", "Cocos (Keeling) Islands"),
    ("CHE", "Switzerland"),
    ("CHL", "Chile"),
    ("CHN", "China"),
    ("CIV", "C\u00f4te d'Ivoire"),
    ("CMR", "Cameroon"),
    ("COD", "Congo (Democratic Republic of the)"),
    ("COG", "Congo"),
    ("COK", "Cook Islands"),
    ("COL", "Colombia"),
    ("COM", "Comoros"),
    ("CPV", "Cabo Verde"),
    ("CRI", "Costa Rica"),
    ("CUB", "Cuba"),
    ("CUW", "Cura\u00e7ao"),
    ("CXR", "Christmas Island"),
    ("CYM", "Cayman Islands"),
    ("CYP", "Cyprus"),
    ("CZE", "Czech Republic"),
    ("DEU", "Germany"),
    ("DJI", "Djibouti"),
    ("DMA", "Dominica"),
    ("DNK", "Denmark"),
    ("DOM", "Dominican Republic"),
    ("DZA", "Algeria"),
    ("ECU", "Ecuador"),
    ("EGY", "Egypt"),
    ("ERI", "Eritrea"),
    ("ESH", "Western Sahara"),
    ("ESP", "Spain"),
    ("EST", "Estonia"),
    ("ETH", "Ethiopia"),
    ("FIN", "Finland"),
    ("FJI", "Fiji"),
    ("FLK", "Falkland Islands (Malvinas)"),
    ("FRA", "France"),
    ("FRO", "Faroe Islands"),
    ("FSM", "Micronesia (Federated States of)"),
    ("GAB", "Gabon"),
    ("GBR", "United Kingdom of Great Britain and Northern Ireland"),
    ("GEO", "Georgia"),
    ("GGY", "Guernsey"),
    ("GHA", "Ghana"),
    ("GIB", "Gibraltar"),
    ("GIN", "Guinea"),
    ("GLP", "Guadeloupe"),
    ("GMB", "Gambia"),
    ("GNB", "Guinea-Bissau"),
    ("GNQ", "Equatorial Guinea"),
    ("GRC", "Greece"),
    ("GRD", "Grenada"),
    ("GRL", "Greenland"),
    ("GTM", "Guatemala"),
    ("GUF", "French Guiana"),
    ("GUM", "Guam"),
    ("GUY", "Guyana"),
    ("HKG", "Hong Kong"),
    ("HMD", "Heard Island and McDonald Islands"),
    ("HND", "Honduras"),
    ("HRV", "Croatia"),
    ("HTI", "Haiti"),
    ("HUN", "Hungary"),
    ("IDN", "Indonesia"),
    ("IMN", "Isle of Man"),
    ("IND", "India"),
    ("IOT", "British Indian Ocean Territory"),
    ("IRL", "Ireland"),
    ("IRN", "Iran (Islamic Republic of)"),
    ("IRQ", "Iraq"),
    ("ISL", "Iceland"),
    ("ISR", "Israel"),
    ("ITA", "Italy"),
    ("JAM", "Jamaica"),
    ("JEY", "Jersey"),
    ("JOR", "Jordan"),
    ("JPN", "Japan"),
    ("KAZ", "Kazakhstan"),
    ("KEN", "Kenya"),
    ("KGZ", "Kyrgyzstan"),
    ("KHM", "Cambodia"),
    ("KIR", "Kiribati"),
    ("KNA", "Saint Kitts and Nevis"),
    ("KOR", "Korea (Republic of)"),
    ("KWT", "Kuwait"),
    ("LAO", "Lao People's Democratic Republic"),
    ("LBN", "Lebanon"),
    ("LBR", "Liberia"),
    ("LBY", "Libya"),
    ("LCA", "Saint Lucia"),
    ("LIE", "Liechtenstein"),
    ("LKA", "Sri Lanka"),
    ("LSO", "Lesotho"),
    ("LTU", "Lithuania"),
    ("LUX", "Luxembourg"),
    ("LVA", "Latvia"),
    ("MAC", "Macao"),
    ("MAF", "Saint Martin (French part)"),
    ("MAR", "Morocco"),
    ("MCO", "Monaco"),
    ("MDA", "Moldova (Republic of)"),
    ("MDG", "Madagascar"),
    ("MDV", "Maldives"),
    ("MEX", "Mexico"),
    ("MHL", "Marshall Islands"),
    ("MKD", "Macedonia (the former Yugoslav Republic of)"),
    ("MLI", "Mali"),
    ("MLT", "Malta"),
    ("MMR", "Myanmar"),
    ("MNE", "Montenegro"),
    ("MNG", "Mongolia"),
    ("MNP", "Northern Mariana Islands"),
    ("MOZ", "Mozambique"),
    ("MRT", "Mauritania"),
    ("MSR", "Montserrat"),
    ("MTQ", "Martinique"),
    ("MUS", "Mauritius"),
    ("MWI", "Malawi"),
    ("MYS", "Malaysia"),
    ("MYT", "Mayotte"),
    ("NAM", "Namibia"),
    ("NCL", "New Caledonia"),
    ("NER", "Niger"),
    ("NFK", "Norfolk Island"),
    ("NGA", "Nigeria"),
    ("NIC", "Nicaragua"),
    ("NIU", "Niue"),
    ("NLD", "Netherlands"),
    ("NOR", "Norway"),
    ("NPL", "Nepal"),
    ("NRU", "Nauru"),
    ("NZL", "New Zealand"),
    ("OMN", "Oman"),
    ("PAK", "Pakistan"),
    ("PAN", "Panama"),
    ("PCN", "Pitcairn"),
    ("PER", "Peru"),
    ("PHL", "Philippines"),
    ("PLW", "Palau"),
    ("PNG", "Papua New Guinea"),
    ("POL", "Poland"),
    ("PRI", "Puerto Rico"),
    ("PRK", "Korea (Democratic People's Republic of)"),
    ("PRT", "Portugal"),
    ("PRY", "Paraguay"),
    ("PSE", "Palestine, State of"),
    ("PYF", "French Polynesia"),
    ("QAT", "Qatar"),
    ("REU", "Reunion"),
    ("ROU", "Romania"),
    ("RUS", "Russian Federation"),
    ("RWA", "Rwanda"),
    ("SAU", "Saudi Arabia"),
    ("SDN", "Sudan"),
    ("SEN", "Senegal"),
    ("SGP", "Singapore"),
    ("SGS", "South Georgia and the South Sandwich Islands"),
    ("SHN", "Saint Helena, Ascension and Tristan da Cunha"),
    ("SJM", "Svalbard and Jan Mayen"),
    ("SLB", "Solomon Islands"),
    ("SLE", "Sierra Leone"),
    ("SLV", "El Salvador"),
    ("SMR", "San Marino"),
    ("SOM", "Somalia"),
    ("SPM", "Saint Pierre and Miquelon"),
    ("SRB", "Serbia"),
    ("SSD", "South Sudan"),
    ("STP", "Sao Tome and Principe"),
    ("SUR", "Suriname"),
    ("SVK", "Slovakia"),
    ("SVN", "Slovenia"),
    ("SWE", "Sweden"),
    ("SWZ", "Swaziland"),
    ("SXM", "Sint Maarten (Dutch part)"),
    ("SYC", "Seychelles"),
    ("SYR", "Syrian Arab Republic"),
    ("TCA", "Turks and Caicos Islands"),
    ("TCD", "Chad"),
    ("TGO", "Togo"),
    ("THA", "Thailand"),
    ("TJK", "Tajikistan"),
    ("TKL", "Tokelau"),
    ("TKM", "Turkmenistan"),
    ("TLS", "Timor-Leste"),
    ("TON", "Tonga"),
    ("TTO", "Trinidad and Tobago"),
    ("TUN", "Tunisia"),
    ("TUR", "Turkey"),
    ("TUV", "Tuvalu"),
    ("TWN", "Taiwan, Province of China"),
    ("TZA", "Tanzania, United Republic of"),
    ("UGA", "Uganda"),
    ("UKR", "Ukraine"),
    ("UMI", "United States Minor Outlying Islands"),
    ("URY", "Uruguay"),
    ("USA", "United States of America"),
    ("UZB", "Uzbekistan"),
    ("VAT", "Holy See"),
    ("VCT", "Saint Vincent and the Grenadines"),
    ("VEN", "Venezuela (Bolivarian Republic of)"),
    ("VGB", "Virgin Islands (British)"),
    ("VIR", "Virgin Islands (U.S.)"),
    ("VNM", "Viet Nam"),
    ("VUT", "Vanuatu"),
    ("WLF", "Wallis and Futuna"),
    ("WSM", "Samoa"),
    ("YEM", "Yemen"),
    ("ZAF", "South Africa"),
    ("ZMB", "Zambia"),
    ("ZWE", "Zimbabwe"),
)

CONTENT_TYPES = (
    ("image/png", "PNG"),
    ("image/jpeg", "JPEG"),
    ("application/pdf", "PDF"),
    ("application/vnd.ms-excel", "xlsx"),
    ("application/msword", "doc"),
    (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document.docx",
        "docx",
    ),
    (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "xlsx",
    ),
    ("text/plain", "text"),
    ("video/mp4", "MP4 Video"),
    ("audio/mp4", "MP4 Audio"),
)


IMAGE_TYPES = ["image/png", "image/jpeg"]

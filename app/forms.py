from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, SelectMultipleField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Optional, Regexp, URL
from app.neo4j_utils import get_eponyms


roman_emperors_list = [('unknown', 'unknown'), ('Augustus', 'Augustus'),
                       ('Tiberius', 'Tiberius'),
                       ('Caligula', 'Caligula'),
                       ('Claudius', 'Claudius'),
                       ('Nero', 'Nero'),
                       ('Galba', 'Galba'),
                       ('Otho', 'Otho'),
                       ('Vitellius', 'Vitellius'),
                       ('Vespasian', 'Vespasian'),
                       ('Titus', 'Titus'),
                       ('Domitian', 'Domitian'),
                       ('Nerva', 'Nerva'),
                       ('Trajan', 'Trajan'),
                       ('Hadrian', 'Hadrian'),
                       ('Antoninus Pius', 'Antoninus Pius'),
                       ('Marc Aurel', 'Marc Aurel'),
                       ('L. Verus', 'L. Verus'),
                       ('Commodus', 'Commodus'),
                       ('Pertinax', 'Pertinax'),
                       ('Didius Iulianus', 'Didius Iulianus'),
                       ('Septimius Severus', 'Septimius Severus'),
                       ('Caracalla', 'Caracalla'),
                       ('Geta', 'Geta'),
                       ('Macrinus', 'Macrinus'),
                       ('Elagabal', 'Elagabal'),
                       ('Severus Alexander', 'Severus Alexander'),
                       ('Maximinus Thrax', 'Maximinus Thrax'),
                       ('Gordian I', 'Gordian I'),
                       ('Gordian II', 'Gordian II'),
                       ('Pupienus', 'Pupienus'),
                       ('Balbinus', 'Balbinus'),
                       ('Gordian III', 'Gordian III'),
                       ('Phillippus Arabs', 'Phillippus Arabs'),
                       ('Decius', 'Decius'),
                       ('Trebonianus Gallus', 'Trebonianus Gallus'),
                       ('Aemilius Aemilianus', 'Aemilius Aemilianus'),
                       ('Valerian', 'Valerian'),
                       ('Gallienus', 'Gallienus'),
                       ('Claudius II Gothicus', 'Claudius II Gothicus'),
                       ('Aurelian', 'Aurelian'),
                       ('Tacitus', 'Tacitus'),
                       ('Probus', 'Probus'),
                       ('Carus', 'Carus'),
                       ('Carinus', 'Carinus'),
                       ('Numerianus', 'Numerianus'),
                       ('Diocletian', 'Diocletian'),
                       ('Maximian', 'Maximian'),
                       ('Constantius I', 'Constantius I'),
                       ('Galerius', 'Galerius'),
                       ('Maximinus Daia', 'Maximinus Daia'),
                       ('Maxentius', 'Maxentius'),
                       ('Licinius', 'Licinius'),
                       ('Constantin I', 'Constantin I'),
                       ('Constantin II', 'Constantin II'),
                       ('Constans I', 'Constans I'),
                       ('Constantius II', 'Constantius II'),
                       ('Julian', 'Julian'),
                       ('Jovian', 'Jovian'),
                       ('Valentinian I', 'Valentinian I'),
                       ('Valens', 'Valens'),
                       ('Gratian', 'Gratian'),
                       ('Valentinian II', 'Valentinian II'),
                       ('Theodosius I', 'Theodosius I'),
                       ]


class CyrenaicaYears(FlaskForm):
    year_reference_system = SelectField('Year Reference System:',
                                        choices=[('None', 'None'),
                                                 ('Unknown', 'Year of Unknown System'),
                                                 ('Era: Actian', 'Actian Era Year'),
                                                 ('Eponymous Officials: Apollo Priest (Cyrenaica)',
                                                  'Eponymous Apollo Priest'),
                                                 ('Regnal: Roman Emperors', 'Regnal Year (Roman Emperor)'),
                                                 ])
    year = StringField('Year:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    apollo_priests_cyrenaica = SelectField('Apollo Priest Cyrenaica',
                                           choices=[('unknown','unknown'),('[--] Κλαύδιος [--]', '[--] Κλαύδιος [--]'),
                                                    ('[--] Πτυλμαίου υἱὸ[ς --]ας', '[--] Πτυλμαίου υἱὸ[ς --]ας'),
                                                    ('[--]ευς Πα[--]', '[--]ευς Πα[--]'),
                                                    ('[--]ευς Πτολεμαῖου υἱὸς Πτολεμαῖος',
                                                     '[--]ευς Πτολεμαῖου υἱὸς Πτολεμαῖος'),
                                                    ('Ἀγχιστ[ρατ-]', 'Ἀγχιστ[ρατ-]'),
                                                    ('Ἀγχίστρατος Καρτισθένευς', 'Ἀγχίστρατος Καρτισθένευς'),
                                                    ('Αἰγλανωρ Πτολεμαίω', 'Αἰγλανωρ Πτολεμαίω'),
                                                    ('Ἄλεξις Καρνήδα', 'Ἄλεξις Καρνήδα'),
                                                    ('Ἀρίσταρχος Θευχρήστω', 'Ἀρίσταρχος Θευχρήστω'),
                                                    ('Ἀριστοτέλης Σώσιος', 'Ἀριστοτέλης Σώσιος'),
                                                    ('Ἄσκλαπος', 'Ἄσκλαπος'),
                                                    ('Ἄσκλαπος Ἰσοκράτους τοῦ Αγχιστράτω',
                                                     'Ἄσκλαπος Ἰσοκράτους τοῦ Αγχιστράτω'),
                                                    ('Ἀσκληπιάδης Ἐπικράτευς', 'Ἀσκληπιάδης Ἐπικράτευς'),
                                                    ('Βαρκαῖος Εὐφάνευς', 'Βαρκαῖος Εὐφάνευς'),
                                                    ('Βαρκαῖος Φίλωνος', 'Βαρκαῖος Φίλωνος'),
                                                    ('Γάιος Ποστόμιος Ὀπτάτος', 'Γάιος Ποστόμιος Ὀπτάτος'),
                                                    ('Διονύσιος Σότα', 'Διονύσιος Σότα'),
                                                    ('Εὐβάτας', 'Εὐβάτας'),
                                                    (
                                                    'Εὐκλείδας Εὐκλείδα τῶ Εὐκλείδα', 'Εὐκλείδας Εὐκλείδα τῶ Εὐκλείδα'),
                                                    ('Εὐκλῆς Αἰγλάνορος', 'Εὐκλῆς Αἰγλάνορος'),
                                                    ('Εὐφάνης Ἰσοκράτευς', 'Εὐφάνης Ἰσοκράτευς'),
                                                    ('Εὐφράνωρ Άντιπάτρω', 'Εὐφράνωρ Άντιπάτρω'),
                                                    ('Ζηνίων Σώσου', 'Ζηνίων Σώσου'),
                                                    ('Θεο[-] Ἀγαθ[-]', 'Θεο[-] Ἀγαθ[-]'),
                                                    ('Θεύχρηστος Διονυσίω', 'Θεύχρηστος Διονυσίω'),
                                                    ('Ἰσοκράτης Ἀγχιστράτω', 'Ἰσοκράτης Ἀγχιστράτω'),
                                                    ('Ἰσοκράτης Κλεάρχω', 'Ἰσοκράτης Κλεάρχω'),
                                                    ('Ἴστρος Ἀγαθίνω', 'Ἴστρος Ἀγαθίνω'),
                                                    ('Ἴστρος Ἴστρω τῶ Ἀγαθίνω', 'Ἴστρος Ἴστρω τῶ Ἀγαθίνω'),
                                                    ('Καρνήδας Ἀλέξιος', 'Καρνήδας Ἀλέξιος'),
                                                    ('Κλέαρχος Εὐφάνευς', 'Κλέαρχος Εὐφάνευς'),
                                                    ('Κλέαρχος Καρνήδα', 'Κλέαρχος Καρνήδα'),
                                                    ('Κλήσιππος', 'Κλήσιππος'),
                                                    ('Κοίντος Φάβιος Καρνεάδης', 'Κοίντος Φάβιος Καρνεάδης'),
                                                    ('Λούκιος', 'Λούκιος'),
                                                    ('Λούκιος Καρνήδας Φλάμμα Ἰσοκράτευς',
                                                     'Λούκιος Καρνήδας Φλάμμα Ἰσοκράτευς'),
                                                    ('Μᾶρκος Αντώνιος Γέμελλος', 'Μᾶρκος Αντώνιος Γέμελλος'),
                                                    ('Μᾶρκος Ἀντώνιος Κασκέλλιος', 'Μᾶρκος Ἀντώνιος Κασκέλλιος'),
                                                    ('Μᾶρκος Ἄντωνιος Κεριάλις Πτολεμαίου τοῦ Πτολεμαίου υἱὸς Αἰγλάνωρ',
                                                     'Μᾶρκος Ἄντωνιος Κεριάλις Πτολεμαίου τοῦ Πτολεμαίου υἱὸς Αἰγλάνωρ'),
                                                    ('Μᾶρκος Ἀντώνιος Μᾶρκου Ἀντωνίου Φλάμμα υἱὸς Ἀριστομένης',
                                                     'Μᾶρκος Ἀντώνιος Μᾶρκου Ἀντωνίου Φλάμμα υἱὸς Ἀριστομένης'),
                                                    ('Μᾶρκος Ἀντώνιου Μᾶρκου Ἀντωνίος Φλάμμα υἱὸς Κασκέλλιος',
                                                     'Μᾶρκος Ἀντώνιου Μᾶρκου Ἀντωνίος Φλάμμα υἱὸς Κασκέλλιος'),
                                                    ('Μᾶρκος Ἀσίνιος Φίλωνος υἱὸς Εὐφράνωρ',
                                                     'Μᾶρκος Ἀσίνιος Φίλωνος υἱὸς Εὐφράνωρ'),
                                                    ('Μᾶρκος Κλέαρχος Φλάμμα Ἰσοκράτευς',
                                                     'Μᾶρκος Κλέαρχος Φλάμμα Ἰσοκράτευς'),
                                                    ('Μητρόδωρος Μητροδώρου τοῦ Μητροδώρου',
                                                     'Μητρόδωρος Μητροδώρου τοῦ Μητροδώρου'),
                                                    ('Νεικόστρατος', 'Νεικόστρατος'),
                                                    ('Ξοῦθος', 'Ξοῦθος'),
                                                    ('Παντα [--]', 'Παντα [--]'),
                                                    ('Πανταλέων Πανταλέοντος', 'Πανταλέων Πανταλέοντος'),
                                                    ('Παυσανίας Φιλίσκω φύσει δὲ Εὐφάνευς',
                                                     'Παυσανίας Φιλίσκω φύσει δὲ Εὐφάνευς'),
                                                    ('Πόπλιος Σήστιος Πολλίων', 'Πόπλιος Σήστιος Πολλίων'),
                                                    ('Πραξιάδας Πραξιἀδα τῶ Φιλίννα', 'Πραξιάδας Πραξιἀδα τῶ Φιλίννα'),
                                                    ('Ῥουτὶλιος', 'Ῥουτὶλιος'),
                                                    ('Σεραπίων Ἀριστάνδρω', 'Σεραπίων Ἀριστάνδρω'),
                                                    ('Σώτας Διονυσίου', 'Σώτας Διονυσίου'),
                                                    ('Τειμαγένης Θευδώρου', 'Τειμαγένης Θευδώρου'),
                                                    ('Τιβέριος Κλαύδιος Ἀρίστανδρος', 'Τιβέριος Κλαύδιος Ἀρίστανδρος'),
                                                    ('Τιβέριος Κλαύδιος Ἀρίστομένης Μᾶγνος ὁ καὶ Περικλῆς',
                                                     'Τιβέριος Κλαύδιος Ἀρίστομένης Μᾶγνος ὁ καὶ Περικλῆς'),
                                                    ('Τιβέριος Κλαύδιος Ἄρχιππος', 'Τιβέριος Κλαύδιος Ἄρχιππος'),
                                                    ('Τιβέριος Κλαύδιος Ἄσκλαπος Φιλίσκου',
                                                     'Τιβέριος Κλαύδιος Ἄσκλαπος Φιλίσκου'),
                                                    ('Τιβέριος Κλαύδιος Ἄτταλος Τιβερίου Κλαυδίου Κλεάρχου υἱὸς',
                                                     'Τιβέριος Κλαύδιος Ἄτταλος Τιβερίου Κλαυδίου Κλεάρχου υἱὸς'),
                                                    ('Τιβέριος Κλαύδιος Ἐπικράτευς υἱὸς Ἀσκλαπιάδας',
                                                     'Τιβέριος Κλαύδιος Ἐπικράτευς υἱὸς Ἀσκλαπιάδας'),
                                                    ('Τιβέριος Κλαύδιος Ἴστρος', 'Τιβέριος Κλαύδιος Ἴστρος'),
                                                    ('Τιβέριος Κλαύδιος Ἴστρος Φιλίσκου',
                                                     'Τιβέριος Κλαύδιος Ἴστρος Φιλίσκου'),
                                                    ('Τιβέριος Κλαύδιος Καρτισθένης Εὐφράνωρ',
                                                     'Τιβέριος Κλαύδιος Καρτισθένης Εὐφράνωρ'),
                                                    ('Τιβέριος Κλαύδιος Κλέαρχος', 'Τιβέριος Κλαύδιος Κλέαρχος'),
                                                    ('Τιβέριος Κλαύδιος Παγκλῆς', 'Τιβέριος Κλαύδιος Παγκλῆς'),
                                                    ('Τιβέριος Κλαύδιος Πρείσκος', 'Τιβέριος Κλαύδιος Πρείσκος'),
                                                    ('Τιβέριος Κλαύδιος Πτολεμαῖος', 'Τιβέριος Κλαύδιος Πτολεμαῖος'),
                                                    ('Τιβέριος Κλαύδιος Τιβερίω Κλαυδίος Ἴστρου υἱὸς Φίλισκος',
                                                     'Τιβέριος Κλαύδιος Τιβερίω Κλαυδίος Ἴστρου υἱὸς Φίλισκος'),
                                                    ('Τιβέριος Κλαύδιος Τιβερίω Κλαυδίω ἀρχιερέος υἱὸς Καρνήδας',
                                                     'Τιβέριος Κλαύδιος Τιβερίω Κλαυδίω ἀρχιερέος υἱὸς Καρνήδας'),
                                                    ('Τιβέριος Κλαύδιος Φιλόξενος Ἀντωνιανός',
                                                     'Τιβέριος Κλαύδιος Φιλόξενος Ἀντωνιανός'),
                                                    ('Τιβέριος Κλαυδίου Φειδίμου υἱὸς Ἴστρος',
                                                     'Τιβέριος Κλαυδίου Φειδίμου υἱὸς Ἴστρος'),
                                                    ('Τίτος Φλάβιος Εὐκλείδας', 'Τίτος Φλάβιος Εὐκλείδας'),
                                                    ('Τίτος Φλάβιος Σαβεῖνος υἱὸς Παυσανίου Παθσανίας',
                                                     'Τίτος Φλάβιος Σαβεῖνος υἱὸς Παυσανίου Παθσανίας'),
                                                    ('Φάβιος Φιλίσκου υἱὸς Φίλιππος', 'Φάβιος Φιλίσκου υἱὸς Φίλιππος'),
                                                    ('Φάος Καρνήδα', 'Φάος Καρνήδα'),
                                                    ('Φάος Κλεάρχω τῶ Φιλοπάτριδος', 'Φάος Κλεάρχω τῶ Φιλοπάτριδος'),
                                                    ('Φίλιππος Ἀριστάνδρω', 'Φίλιππος Ἀριστάνδρω'),
                                                    ('Φίλισκος Φιλίσκου φύσει δὲ Εὐφάνευς',
                                                     'Φίλισκος Φιλίσκου φύσει δὲ Εὐφάνευς'),
                                                    ('Φιλόξενος Φιλίσπω φύσει δὲ Εὐφάνευς',
                                                     'Φιλόξενος Φιλίσπω φύσει δὲ Εὐφάνευς'),
                                                    ('Φιλων Ἀγαθίνω', 'Φιλων Ἀγαθίνω'),
                                                    ('Φίλων Εὐφράνορος', 'Φίλων Εὐφράνορος'),
                                                    ('Φίλων Φιλοκώμω', 'Φίλων Φιλοκώμω'),
                                                    ('Φλάμμας', 'Φλάμμας'),
                                                    ])
    roman_emperors = SelectField('Roman Emperor:',
                                 choices=roman_emperors_list)
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                           choices=[('None', 'None'),
                                                    ('Thot', 'Thot'),
                                                    ('Phaophi', 'Phaophi'),
                                                    ('Hathyr', 'Hathyr'),
                                                    ('Choiak', 'Choiak'),
                                                    ('Tybi', 'Tybi'),
                                                    ('Mecheir', 'Mecheir'),
                                                    ('Phamenoth', 'Phamenoth'),
                                                    ('Pharmuthi', 'Pharmuthi'),
                                                    ('Pachons', 'Pachons'),
                                                    ('Payni', 'Payni'),
                                                    ('Epeiph', 'Epeiph'),
                                                    ('Mesore', 'Mesore'),
                                                    ('Epagomenal Days', 'Epagomenal Days'),
                                                    ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    attestation_uri = StringField('Attestation URI:', validators=[DataRequired()])
    date_string = StringField('Date String:', validators=[DataRequired()])
    title = StringField('Title:', validators=[DataRequired()])
    date_category = SelectField('Date Category:',
                                        choices=[('',''),
                                                 ('Uncategorised', 'Uncategorised'),
                                                 ('Date of Death', 'Date of Death'),
                                                 ('Date of Birth', 'Date of Birth'),
                                                 ('Date of Document', 'Date of Document'),
                                                 ('Date of Recording', 'Date of Recording'),
                                                 ('Date of Action', 'Date of Action'),
                                                 ('Date of Office', 'Date of Office'),
                                                 ('Recurring Date of Action', 'Recurring Date of Action (Feasts, etc.)'),
                                                 ('Roman Emperor Titulature', 'Roman Emperor Titulature'),
                                                 ])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class AttestationUpdate(FlaskForm):
    attestation_uri = StringField('Attestation URI:', validators=[DataRequired()])
    date_string = StringField('Date String:', validators=[DataRequired()])
    title = StringField('Title:', validators=[DataRequired()])
    date_category = SelectField('Date Category:',
                                choices=[('', ''),
                                         ('Uncategorised', 'Uncategorised'),
                                         ('Date of Death', 'Date of Death'),
                                         ('Date of Birth', 'Date of Birth'),
                                         ('Date of Document', 'Date of Document'),
                                         ('Date of Recording', 'Date of Recording'),
                                         ('Date of Action', 'Date of Action'),
                                         ('Date of Office', 'Date of Office'),
                                         ('Recurring Date of Action', 'Recurring Date of Action (Feasts, etc.)'),
                                         ('Roman Emperor Titulature', 'Roman Emperor Titulature'),
                                         ])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class AttestationDelete(FlaskForm):
    submit = SubmitField('Delete...')


class SearchRomanConsulate(FlaskForm):
    consulship = StringField('Consulship:', validators=[DataRequired()])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class EgyptianCalendarLatePeriod(FlaskForm):
    late_period_pharaos = SelectField('Reign:',
                                      choices=[('1','Psametik I, years 1-55'),
                                               ('2', 'Necho, years 1-16'),
                                               ('3', 'Psametik II, years 1-7'),
                                               ('4', 'Apries, years 1-20'),
                                               ('5', 'Amasis, years 1-45'),
                                               ('6', 'Psametik III, years 1-2'),
                                               ('7', 'Cambyses, years 1-4'),
                                               ('8', 'Darius I, years 1-36'),
                                               ('9', 'Xerxes I, years 1-21'),
                                               ('10', 'Artaxerxes, years 1-42'),
                                               ('11', 'Darius II, years 1-20'),
                                               ('12', 'Artaxerxes II, years 1-4'),
                                               ('13', 'Amyrtaeos, years 1-6'),
                                               ('14', 'Nepherites I, years 1-7'),
                                               ('15', 'Achoris, years 1-14'),
                                               ('16', 'Psammuthis, year 1'),
                                               ('17', 'Nepherites II, year 1'),
                                               ('18', 'Nektanebo I, years 1-19'),
                                               ('19', 'Theos, years 1-5'),
                                               ('20', 'Nektanebo II, years 1-18'),
                                               ('21', 'Artaxerxes III, years 1-6'),
                                               ('22', 'Arses, years 1-2'),
                                               ('23', 'Darius III, years 1-6'),
                                               ('24', 'Khababash, years 1-3'),
                                               ])
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                           choices=[('0', 'None'),
                                                    ('1', 'Thot'),
                                                    ('2', 'Phaophi'),
                                                    ('3', 'Hathyr'),
                                                    ('4', 'Choiak'),
                                                    ('5', 'Tybi'),
                                                    ('6', 'Mecheir'),
                                                    ('7', 'Phamenoth'),
                                                    ('8', 'Pharmuthi'),
                                                    ('9', 'Pachons'),
                                                    ('10', 'Payni'),
                                                    ('11', 'Epeiph'),
                                                    ('12', 'Mesore'),
                                                    ('13', 'Epagomenal Days'),
                                                    ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    year = IntegerField('Year:', validators=[
        DataRequired()])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class EgyptianCalendarPtolemies(FlaskForm):
    ptolemaic_pharaos = SelectField('Reign:',
                                      choices=[('1','Alexander III (the Great), years 1-9'),
                                               ('2', 'Philip Arrhidaeus, years 1-8'),
                                               ('3', 'Alexander IV, years 1-13'),
                                               ('4', 'Ptolemy I Soter, years 1-21'),
                                               ('5', 'Ptolemy II Philadelphus, years 1-39'),
                                               ('6', 'Ptolemy III Euergetes, years 1-26'),
                                               ('7', 'Ptolemy IV Philopator, years 1-18'),
                                               ('8', 'Ptolemy V Epiphanes, years 1-25'),
                                               ('9', 'Ptolemy VI Philometor, years 1-12'),
                                               ('10', 'Ptolemy VI Philometor, Ptolemy VIII (Euergetes II), Cleopatra II, years 1-7 / 12-18'),
                                               ('11', 'Ptolemy VIII (Euergetes II) alone, year 7'),
                                               ('12', 'Ptolemy VI Philometor and Cleopatra II restored, years 18-36'),
                                               ('13', 'Ptolemy VII Neos Philopator, year 1'),
                                               ('14', 'Ptolemy VIII Euergetes II restored, years 25-54'),
                                               ('15', 'Cleopatra III and Ptolemy IX Soter II (Lathyros), years 1-11'),
                                               ('16', 'Cleopatra III and Ptolemy X Alexander I, years 11-17'),
                                               ('17', 'Ptolemy X Alexander I and Cleopatra III, years 8-14'),
                                               ('18', 'Ptolemy X Alexander I and Cleopatra Berenice, years 14-27'),
                                               ('19', 'Ptolemy IX Soter II (Lathyros) restored, years 30-37'),
                                               ('20', 'Cleopatra Berenice (afterwards with Ptolemy XI Alexander II), year 1'),
                                               ('21', 'Ptolemy XII Neos Dionysos (Auletes), years 1-24'),
                                               ('22', 'Berenice IV (at first with Cleopatra Tryphaena), years 1-2'),
                                               ('23', 'Berenice IV and Archelaus, years 2-3'),
                                               ('24', 'Archelaus and Berenice IV, years 1-2'),
                                               ('25', 'Ptolemy XII Neos Dionysos (Auletes) restored, years 26-30'),
                                               ('26', 'Cleopatra VII Philopator, years 1-22'),
                                               ])
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                           choices=[('0', 'None'),
                                                    ('1', 'Thot'),
                                                    ('2', 'Phaophi'),
                                                    ('3', 'Hathyr'),
                                                    ('4', 'Choiak'),
                                                    ('5', 'Tybi'),
                                                    ('6', 'Mecheir'),
                                                    ('7', 'Phamenoth'),
                                                    ('8', 'Pharmuthi'),
                                                    ('9', 'Pachons'),
                                                    ('10', 'Payni'),
                                                    ('11', 'Epeiph'),
                                                    ('12', 'Mesore'),
                                                    ('13', 'Epagomenal Days'),
                                                    ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    year = IntegerField('Year:', validators=[
        DataRequired()])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class EgyptianCalendarRomanEmperors(FlaskForm):
    roman_emperors = SelectField('Reign:',
                                      choices=[ ('1', 'Augustus, years 1-43'),
                                                ('2', 'Tiberius, years 1-23'),
                                                ('3', 'Caligula, years 1-5'),
                                                ('4', 'Claudius, years 1-15'),
                                                ('5', 'Nero, years 1-14'),
                                                ('6', 'Galba, years 1-2'),
                                                ('7', 'Otho, year 1'),
                                                ('8', 'Vitellius, years 1-2'),
                                                ('9', 'Vespasian, years 1-11'),
                                                ('10', 'Titus, years 1-4'),
                                                ('11', 'Domitian, years 1-16'),
                                                ('12', 'Nerva, years 1-2'),
                                                ('13', 'Traian, years 1-20'),
                                                ('14', 'Hadrian, years 1-22'),
                                                ('15', 'Antoninus Pius, years 1-24'),
                                                ('16', 'Marc Aurel, years 1-20'),
                                                ('17', 'Commodus, years 20-33'),
                                                ('18', 'Pertinax, year 1'),
                                                ('19', 'Pescennius Niger, years 1-2'),
                                                ('20', 'Septimius Severus, years 1-19'),
                                                ('21', 'Caracalla, years 19-25'),
                                                ('22', 'Macrinus, years 1-2'),
                                                ('23', 'Elagabal, years 1-5'),
                                                ('24', 'Severus Alexander, years 1-14'),
                                                ('25', 'Maximinus Thrax, years 1-4'),
                                                ('26', 'Gordian, years 1-7'),
                                                ('27', 'Phillipus Arabs, years 1-7'),
                                                ('28', 'Decius, years 1-2'),
                                                ('29', 'Gallus / Volusianus, years 1-3'),
                                                ('30', 'Aemilian, years 1-2'),
                                                ('31', 'Valerian / Gallienus, years 1-8'),
                                                ('32', 'Macrianus / Quietus, years 1-2'),
                                                ('33', 'Gallienus, years 9-16'),
                                                ('34', 'Claudius Gothicus, years 1-2'),
                                                ('35', 'Aurelian, years 1-7'),
                                                ('36', 'Tacitus, year 1'),
                                                ('37', 'Probus, years 1-7'),
                                                ('38', 'Carus / Carinus, years 1-3'),
                                                ('39', 'Diocletian, years 1 ff.'),
                                               ])
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                           choices=[('0', 'None'),
                                                    ('1', 'Thot'),
                                                    ('2', 'Phaophi'),
                                                    ('3', 'Hathyr'),
                                                    ('4', 'Choiak'),
                                                    ('5', 'Tybi'),
                                                    ('6', 'Mecheir'),
                                                    ('7', 'Phamenoth'),
                                                    ('8', 'Pharmuthi'),
                                                    ('9', 'Pachons'),
                                                    ('10', 'Payni'),
                                                    ('11', 'Epeiph'),
                                                    ('12', 'Mesore'),
                                                    ('13', 'Epagomenal Days'),
                                                    ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    year = IntegerField('Year:', validators=[
        DataRequired()])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class RomanConsularDating(FlaskForm):
    consulship = StringField('Consulship:', validators=[DataRequired()])
    day_ref = SelectField('Kalends/Nones/Ides:',
                          choices=[('Kalends', 'Kalends'),
                                   ('Nones', 'Nones'),
                                   ('Ides', 'Ides'),
                                   ])
    months = SelectField('Month:',
                         choices=[('January', 'January'),
                                  ('February', 'February'),
                                  ('March', 'March'),
                                  ('April', 'April'),
                                  ('May', 'May'),
                                  ('June', 'June'),
                                  ('July', 'July'),
                                  ('August', 'August'),
                                  ('September', 'September'),
                                  ('October', 'October'),
                                  ('November', 'November'),
                                  ('December', 'December'),
                                  ])
    day_number = SelectField('Day:',
                             choices=[
                                 (1, ''),
                                 (2, 'a.d. II (pridie)'),
                                 (3, 'a.d. III'),
                                 (4, 'a.d. IV'),
                                 (5, 'a.d. V'),
                                 (6, 'a.d. VI'),
                                 (7, 'a.d. VII'),
                                 (8, 'a.d. VIII'),
                                 (9, 'a.d. IX'),
                                 (10, 'a.d. X'),
                                 (11, 'a.d. XI'),
                                 (12, 'a.d. XII'),
                                 (13, 'a.d. XIII'),
                                 (14, 'a.d. XIV'),
                                 (15, 'a.d. XV'),
                                 (16, 'a.d. XVI'),
                                 (17, 'a.d. XVII'),
                                 (18, 'a.d. XVIII'),
                                 (19, 'a.d. XIX'),
                             ])
    reset = SubmitField('Reset...')
    submit = SubmitField('Convert...')


class CyrenaicaRomanImperialTitulature(FlaskForm):
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')
    attestation_uri = StringField('Attestation URI:', validators=[DataRequired()])
    date_string = StringField('Date String:', validators=[DataRequired()])
    title = StringField('Title:', validators=[DataRequired()])
    date_category = SelectField('Date Category:',
                                choices=[('', ''),
                                         ('Uncategorised', 'Uncategorised'),
                                         ('Date of Death', 'Date of Death'),
                                         ('Date of Birth', 'Date of Birth'),
                                         ('Date of Document', 'Date of Document'),
                                         ('Date of Recording', 'Date of Recording'),
                                         ('Date of Action', 'Date of Action'),
                                         ('Date of Office', 'Date of Office'),
                                         ('Recurring Date of Action', 'Recurring Date of Action (Feasts, etc.)'),
                                         ('Roman Emperor Titulature', 'Roman Emperor Titulature'),
                                         ])
    roman_emperors = SelectField('Roman Emperor:',
                                 choices=roman_emperors_list)
    egyptian_calendar_months = SelectField('Months (Egyptian):',
                                           choices=[('None', 'None'),
                                                    ('Thot', 'Thot'),
                                                    ('Phaophi', 'Phaophi'),
                                                    ('Hathyr', 'Hathyr'),
                                                    ('Choiak', 'Choiak'),
                                                    ('Tybi', 'Tybi'),
                                                    ('Mecheir', 'Mecheir'),
                                                    ('Phamenoth', 'Phamenoth'),
                                                    ('Pharmuthi', 'Pharmuthi'),
                                                    ('Pachons', 'Pachons'),
                                                    ('Payni', 'Payni'),
                                                    ('Epeiph', 'Epeiph'),
                                                    ('Mesore', 'Mesore'),
                                                    ('Epagomenal Days', 'Epagomenal Days'),
                                                    ])
    day = StringField('Day:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    consul_number = StringField('Consul Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    consul_designatus = BooleanField('consul designatus')
    trib_pot_number = StringField('Trib Pot Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    imperator_number = StringField('Imperator Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    victory_titles = SelectMultipleField('Victory Titles:',
                                         choices=[
                                             ('Adiabenicus 1', 'Adiabenicus'),
                                             ('Adiabenicus max. 1', 'Adiabenicus max.'),
                                             ('Aegyptiacus max. 1', 'Aegyptiacus max.'),
                                             ('Alamannicus max. 1', 'Alamannicus max.'),
                                             ('Arabicus 1', 'Arabicus'),
                                             ('Arabicus max. 1', 'Arabicus max.'),
                                             ('Armeniacus 1', 'Armeniacus'),
                                             ('Armeniacus max. 1', 'Armeniacus max.'),
                                             ('Britannicus 1', 'Britannicus'),
                                             ('Britannicus max. 1', 'Britannicus max.'),
                                             ('Britannicus max. 2', 'Britannicus max. 2'),
                                             ('Carpicus max. 1', 'Carpicus max.'),
                                             ('Carpicus max. 2', 'Carpicus max. 2'),
                                             ('Carpicus max. 3', 'Carpicus max. 3'),
                                             ('Carpicus max. 4', 'Carpicus max. 4'),
                                             ('Carpicus max. 5', 'Carpicus max. 5'),
                                             ('Carpicus max. 6', 'Carpicus max. 6'),
                                             ('Dacicus 1', 'Dacicus'),
                                             ('Dacicus max. 1', 'Dacicus max.'),
                                             ('Francicus max. 1', 'Francicus max.'),
                                             ('Germanicus 1', 'Germanicus'),
                                             ('Germanicus max. 1', 'Germanicus max.'),
                                             ('Germanicus max. 2', 'Germanicus max. 2'),
                                             ('Germanicus max. 3', 'Germanicus max. 3'),
                                             ('Germanicus max. 4', 'Germanicus max. 4'),
                                             ('Germanicus max. 5', 'Germanicus max. 5'),
                                             ('Germanicus max. 6', 'Germanicus max. 6'),
                                             ('Germanicus max. 7', 'Germanicus max. 7'),
                                             ('Gothicus 1', 'Gothicus'),
                                             ('Gothicus max. 1', 'Gothicus max.'),
                                             ('Gothicus max. 2', 'Gothicus max. 2'),
                                             ('Medicus 1', 'Medicus'),
                                             ('Medicus max. 1', 'Medicus max.'),
                                             ('Palmyrenicus max. 1', 'Palmyrenicus max.'),
                                             ('Parthicus 1', 'Parthicus'),
                                             ('Parthicus max. 1', 'Parthicus max.'),
                                             ('Parthicus Arabicus 1', 'Parthicus Arabicus'),
                                             ('Parthicus Adiabenicus 1', 'Parthicus Adiabenicus'),
                                             ('Persicus 1', 'Persicus'),
                                             ('Persicus max. 1', 'Persicus max.'),
                                             ('Persicus max. 2', 'Persicus max. 2'),
                                             ('Persicus max. 3', 'Persicus max. 3'),
                                             ('Sarmaticus 1', 'Sarmaticus'),
                                             ('Sarmaticus max. 1', 'Sarmaticus max.'),
                                             ('Sarmaticus max. 2', 'Sarmaticus max. 2'),
                                             ('Sarmaticus max. 3', 'Sarmaticus max. 3'),
                                             ('Sarmaticus max. 4', 'Sarmaticus max. 4'),
                                             ('Sarmaticus max. 5', 'Sarmaticus max. 5'),
                                             ('Thebaicus max. 1', 'Thebaicus max.'),
                                         ])


class RomanImperialDating(FlaskForm):
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')
    consul_number = StringField('Consul Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    consul_designatus = BooleanField('consul designatus')
    trib_pot_number = StringField('Trib Pot Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    imperator_number = StringField('Imperator Number:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    victory_titles = SelectMultipleField('Victory Titles:',
                                         choices=[
                                             ('Adiabenicus 1', 'Adiabenicus'),
                                             ('Adiabenicus max. 1', 'Adiabenicus max.'),
                                             ('Aegyptiacus max. 1', 'Aegyptiacus max.'),
                                             ('Alamannicus max. 1', 'Alamannicus max.'),
                                             ('Arabicus 1', 'Arabicus'),
                                             ('Arabicus max. 1', 'Arabicus max.'),
                                             ('Armeniacus 1', 'Armeniacus'),
                                             ('Armeniacus max. 1', 'Armeniacus max.'),
                                             ('Britannicus 1', 'Britannicus'),
                                             ('Britannicus max. 1', 'Britannicus max.'),
                                             ('Britannicus max. 2', 'Britannicus max. 2'),
                                             ('Carpicus max. 1', 'Carpicus max.'),
                                             ('Carpicus max. 2', 'Carpicus max. 2'),
                                             ('Carpicus max. 3', 'Carpicus max. 3'),
                                             ('Carpicus max. 4', 'Carpicus max. 4'),
                                             ('Carpicus max. 5', 'Carpicus max. 5'),
                                             ('Carpicus max. 6', 'Carpicus max. 6'),
                                             ('Dacicus 1', 'Dacicus'),
                                             ('Dacicus max. 1', 'Dacicus max.'),
                                             ('Francicus max. 1', 'Francicus max.'),
                                             ('Germanicus 1', 'Germanicus'),
                                             ('Germanicus max. 1', 'Germanicus max.'),
                                             ('Germanicus max. 2', 'Germanicus max. 2'),
                                             ('Germanicus max. 3', 'Germanicus max. 3'),
                                             ('Germanicus max. 4', 'Germanicus max. 4'),
                                             ('Germanicus max. 5', 'Germanicus max. 5'),
                                             ('Germanicus max. 6', 'Germanicus max. 6'),
                                             ('Germanicus max. 7', 'Germanicus max. 7'),
                                             ('Gothicus 1', 'Gothicus'),
                                             ('Gothicus max. 1', 'Gothicus max.'),
                                             ('Gothicus max. 2', 'Gothicus max. 2'),
                                             ('Medicus 1', 'Medicus'),
                                             ('Medicus max. 1', 'Medicus max.'),
                                             ('Palmyrenicus max. 1', 'Palmyrenicus max.'),
                                             ('Parthicus 1', 'Parthicus'),
                                             ('Parthicus max. 1', 'Parthicus max.'),
                                             ('Parthicus Arabicus 1', 'Parthicus Arabicus'),
                                             ('Parthicus Adiabenicus 1', 'Parthicus Adiabenicus'),
                                             ('Persicus 1', 'Persicus'),
                                             ('Persicus max. 1', 'Persicus max.'),
                                             ('Persicus max. 2', 'Persicus max. 2'),
                                             ('Persicus max. 3', 'Persicus max. 3'),
                                             ('Sarmaticus 1', 'Sarmaticus'),
                                             ('Sarmaticus max. 1', 'Sarmaticus max.'),
                                             ('Sarmaticus max. 2', 'Sarmaticus max. 2'),
                                             ('Sarmaticus max. 3', 'Sarmaticus max. 3'),
                                             ('Sarmaticus max. 4', 'Sarmaticus max. 4'),
                                             ('Sarmaticus max. 5', 'Sarmaticus max. 5'),
                                             ('Thebaicus max. 1', 'Thebaicus max.'),
                                         ])


class EponymOffice(FlaskForm):
    pleiades_uri = StringField('Pleiades URI:', validators=[URL(), DataRequired()])
    wikidata_uri = StringField('Wikidata URI of Office:', validators=[Optional(), URL()])
    godot_uri = StringField('GODOT URI:')
    place_label = StringField('Place Label:', validators=[DataRequired()])
    type = StringField('Type of Office:', validators=[DataRequired()])
    description = TextAreaField('Description of Office:')
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')


class EponymOfficial(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    wikidata_uri = StringField('Wikidata URI of Official:', validators=[Optional(), URL()])
    identifying_uri = StringField('Identifying URI of Official:', validators=[Optional()])
    snap_uri = StringField('SNAP URI of Official:', validators=[Optional(), URL()])
    office_godot_uri = StringField('Office GODOT URI:')
    official_godot_uri = StringField('Official GODOT URI:')
    not_before = StringField('Not Before Year:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    not_after = StringField('Not After Year:', validators=[
        Optional(), Regexp('^[0-9_]*$')])
    reset = SubmitField('Reset...')
    submit = SubmitField('Submit...')

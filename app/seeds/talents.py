from app.models import db, environment, SCHEMA
from app.models.talent import Talent
from sqlalchemy.sql import text

def seed_talents():
    try:
        # Core Rulebook
        airOfAuthority = Talent(
            talent_name='Air of Authority',
            talent_desc="You exude a natural aura of command, instilling subservience in all around you. On a successful command test, you may affect a number of targets equal to 1d10 plus your fellowship bonus. Such is the authority in your voice that even those who are not in your service jump to attention when you speak. You may attempt to get non-servants to follow your commands by making a command test with a -10 penalty."
        )
        ambidexterous = Talent(
            talent_name='Ambidexterous',
            talent_desc='You can use either hand equally well. You do not take the normal -20 penalty for making attacks with your secondary hand. If you have the Two-Weapon Wielder talent, the penalty for making attacks with both weapons in the same turn drops to -10.'
        )
        armorOfContempt = Talent(
            talent_name='Armor of Contempt',
            talent_desc='You drape yourself in the armor of scorn and hatred. Whenever you would gain corruption points, reduce the amount you would gain by 1. In addition, you may test willpower as a free action to ignore the effects of accumulated corruption for 1 round.'
        )
        armsMaster = Talent(
            talent_name='Arms Master',
            talent_desc='Such is your skill with a gun that you are able to pick up an unfamiliar weapon and use it as though you had trained with it for years. You can use ranged weapons you do not have training in at a -10 penalty rather than the standard -20.'
        )
        assassinStrike = Talent(
            talent_name='Assassin Strike',
            talent_desc='You are like a serene dancer when engaged in combat, leaping and spiralling between dismembered corpses like some butcher ballerina. Whenever you engage an opponent and make a melee attack, you may make an acrobatics test to move at your half move rate as a free action. Your opponent may not take the customary free attack.'
        )
        autosanguine = Talent(
            talent_name='Autosanguine',
            talent_desc='Ancient and blessed technology filters your blood. Handed down from generations past, your implants repair minor injuries. For the purposes of healing, you are always considered to be lightly wounded. In addition, you naturally heal at an increased rate, removing two points of damage each day. Your autosanguinators also sooth the minor pains and sores caused by the blessed metal of your implants pressing upon your weak flesh. This has no in-game effect, but makes you slightly less irritable than before.'
        )
        basicWeaponTrainingBolt = Talent(
            talent_name='Basic Weapon Training (Bolt)',
            talent_desc='You have received basic weapon training in bolt weapons and can use them without penalty.'
        )
        basicWeaponTrainingFlame = Talent(
            talent_name='Basic Weapon Training (Flame)',
            talent_desc='You have received basic weapon training in flame weapons and can use them without penalty.'
        )
        basicWeaponTrainingLas = Talent(
            talent_name='Basic Weapon Training (Las)',
            talent_desc='You have received basic weapon training in las weapons and can use them without penalty.'
        )
        basicWeaponTrainingLauncher = Talent(
            talent_name='Basic Weapon Training (Launcher)',
            talent_desc='You have received basic weapon training in launcher weapons and can use them without penalty.'
        )
        basicWeaponTrainingMelta = Talent(
            talent_name='Basic Weapon Training (Melta)',
            talent_desc='You have received basic weapon training in melta weapons and can use them without penalty.'
        )
        basicWeaponTrainingPlasma = Talent(
            talent_name='Basic Weapon Training (Plasma)',
            talent_desc='You have received basic weapon training in plasma weapons and can use them without penalty.'
        )
        basicWeaponTrainingPrimitive = Talent(
            talent_name='Basic Weapon Training (Primitive)',
            talent_desc='You have received basic weapon training in primitive weapons and can use them without penalty.'
        )
        basicWeaponTrainingSP = Talent(
            talent_name='Basic Weapon Training (SP)',
            talent_desc='You have received basic weapon training in solid projectile weapons and can use them without penalty.'
        )
        battleRage = Talent(
            talent_name='Battle Rage',
            talent_desc='Despite your frenzied nature, you remain in control when engaging in melee. You can spend reactions to parry when frenzied.'
        )
        berserkCharge = Talent(
            talent_name='Berserk Charge',
            talent_desc='You hurl yourself at your enemies with reckless abandon, using the force of your charge to add force to your strikes. When you make a charge manuver you gain a +20 bonus to your weapon skill instead of the typical +10.'
        )
        binaryChatter = Talent(
            talent_name='Binary Chatter',
            talent_desc='You are adept at controlling servitors. Gain a +10 bonus to any attempt to instruct, program, or question servitors.'
        )
        blademaster = Talent(
            talent_name='Blademaster',
            talent_desc='Your mastery of sword and knife is unsurpassed and your blade always strikes true. When attacking with a sword or knife, including chain swords and power swords, you may re-roll a missed attack once per round.'
        )
        blindFighting = Talent(
            talent_name='Blind Fighting',
            talent_desc='Through years of practice and heightening your senses, you no longer need to be able to see your opponents to be able to hit them. You take half the usual penalties when fighting in environments that obscure your vision, such as fog, smoke, and darkness.'
        )
        bulgingBiceps = Talent(
            talent_name='Bulging Biceps',
            talent_desc='Wheras a weaker individual would be sent flying when using powerful weapons, your strong physique allows you to remain standing. You can fire a heavy weapon on semi-automatic or automatic modes without bracing first.'
        )
        catfall = Talent(
            talent_name='Catfall',
            talent_desc='You are nimble and balanced, like a cat, and are able to fall much greater distances unharmed than others might. Whenever you fall, you may test your agility as a free action. On success, remove the product of your agility bonus times the degrees of success from the distance fallen for the purposes of determining damage suffered from the fall.'
        )
        chemGeld = Talent(
            talent_name='Chem Geld',
            talent_desc='A variety of chemical and surgical treatments have rendered you immune to the temptations of the flesh. Seduction attempts against you automatically fail and the difficulty of all charm tests against you increase by one step (A challenging (+0) test becomes difficult(-10) and so on). When you take this talent you gain one insanity point.'
        )
        cleanseAndPurify = Talent(
            talent_name='Cleanse and Purify',
            talent_desc='Burn! Burn! Burn! None shall escape your fiery wrath! Targets exposed to your flamer attacks take a -20 penatly to avoid being hit.'
        )
        combatMaster = Talent(
            talent_name='Combat Master',
            talent_desc='Through a combination of reflex and perception you are able to keep many more opponents at bay in melee than a lesser skilled combatant might. Opponents fighting you in hand-to-hand combat gain no bonuses for outnumbering you.'
        )
        concealedCavity = Talent(
            talent_name='Concealed Cavity',
            talent_desc='You have a small compartment hidden upon your person. This might be a pouch within your flesh or a chamber fitted into one of your cybernetic implants. You may conceal a small item, no larger than the palm of your hand, within this cavity. The compartment may be discovered on a difficult (-10) search test. If the searcher employs additional technology, such as a medicae scanner or chem-sniffer, this difficulty is reduced to ordinary (+10).'
        )
        corpusConversion = Talent(
            talent_name='Corpus Conversion',
            talent_desc='You can siphon the health of your physical body to fuel your powers. For every 2 points of damage you voluntarily take, you may add your willpower bonus to your power roll. Using this talent is a free action.'
        )
        counterAttack = Talent(
            talent_name='Counter-Attack',
            talent_desc="You are skilled at switching from defence to attack in the blink of an eye. When you successfully parry an opponent's attack, you may immediately make an attack against that opponent using the weapon with whcih you parried. This attack takes a -20 penalty to the test."
        )
        crachShot = Talent(
            talent_name='Crack Shot',
            talent_desc='You are able to target your shots at the places where they will inflict more harm. When your ranged attacks deal critical damage, you deal an extra 2 points.'
        )
        cripplingStrike = Talent(
            talent_name='Crippling Strike',
            talent_desc='You are able to land your blows in the spot where they will inflict the most harm. Whenever you deal critical damage to an opponent using a melee weapon, you may deal an additional 1d5-1 points.'
        )

        db.session.add(airOfAuthority)
        db.session.add(ambidexterous)
        db.session.add(armorOfContempt)
        db.session.add(armsMaster)
        db.session.add(assassinStrike)
        db.session.add(autosanguine)
        db.session.add(basicWeaponTrainingBolt)
        db.session.add(basicWeaponTrainingFlame)
        db.session.add(basicWeaponTrainingLas)
        db.session.add(basicWeaponTrainingLauncher)
        db.session.add(basicWeaponTrainingMelta)
        db.session.add(basicWeaponTrainingPlasma)
        db.session.add(basicWeaponTrainingPrimitive)
        db.session.add(basicWeaponTrainingSP)
        db.session.add(battleRage)
        db.session.add(berserkCharge)
        db.session.add(binaryChatter)
        db.session.add(blademaster)
        db.session.add(blindFighting)
        db.session.add(bulgingBiceps)
        db.session.add(catfall)
        db.session.add(chemGeld)
        db.session.add(cleanseAndPurify)
        db.session.add(combatMaster)
        db.session.add(concealedCavity)
        db.session.add(corpusConversion)
        db.session.add(counterAttack)
        db.session.add(crachShot)
        db.session.add(cripplingStrike)
        db.session.commit()
    except Exception as e:
        print('-------------------------------------------------------')
        print(f"Error seeding talents: {e}")
        print('-------------------------------------------------------')
        db.session.rollback()

def undo_talents():
    if environment == 'production':
        db.session.execute(f"TRUNCATE table {SCHEMA}.games RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM talents"))

    db.session.commit()

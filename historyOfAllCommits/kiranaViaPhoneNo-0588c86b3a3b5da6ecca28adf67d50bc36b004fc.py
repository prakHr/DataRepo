#kirana with phoneNo=>919809258989,+918290023496,+918008485850,+918432520108,+917020572289
def NumberInt(x):return int(x)
def NumberLong(x):return (0)
#instead of parsing from txt file put into myarray for right now
myarray= [
        {
            "barcodeName" : "Wonder soft hair color", 
            "barcodeNumber" : "1234567891231", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Sored socolor.beauty", 
            "barcodeNumber" : "3474630444638", 
            "barcodePrice" : NumberInt(360), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nivea total face wash", 
            "barcodeNumber" : "4005808918362", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nivea total face cleanup", 
            "barcodeNumber" : "4005900195821", 
            "barcodePrice" : NumberInt(210), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Ambi pur air effects rose blossom", 
            "barcodeNumber" : "4902430662420", 
            "barcodePrice" : NumberInt(285), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "vick's vaporub", 
            "barcodeNumber" : "4987176013866", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "vick's vaporub ", 
            "barcodeNumber" : "4987176014894", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "India gate basmati rice tibar ", 
            "barcodeNumber" : "690225101127", 
            "barcodePrice" : NumberInt(124)
        }, 
        {
            "barcodeName" : "India gate basmati rice dubar", 
            "barcodeNumber" : "690225101134", 
            "barcodePrice" : NumberInt(111)
        }, 
        {
            "barcodeName" : "India gate basmati rice tibar", 
            "barcodeNumber" : "690225103121", 
            "barcodePrice" : NumberInt(625)
        }, 
        {
            "barcodeName" : "india gaye basmati rice dubar", 
            "barcodeNumber" : "690225103138", 
            "barcodePrice" : NumberInt(470), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "India gate basmati rice feast rozzana", 
            "barcodeNumber" : "690225103626", 
            "barcodePrice" : NumberInt(98), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Indian gate basmati rice feast rozzana", 
            "barcodeNumber" : "690225103633", 
            "barcodePrice" : NumberInt(485)
        }, 
        {
            "barcodeName" : "India gate basmati rice mogra ", 
            "barcodeNumber" : "690225103718", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "India gate basmati rice mini mogra", 
            "barcodeNumber" : "690225104197", 
            "barcodePrice" : NumberInt(570)
        }, 
        {
            "barcodeName" : "India gate basmati rice mogra", 
            "barcodeNumber" : "690225106092", 
            "barcodePrice" : NumberInt(375)
        }, 
        {
            "barcodeName" : "India gate basmati rice regular choice", 
            "barcodeNumber" : "690225106474", 
            "barcodePrice" : NumberInt(445), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "India gate brown rice ", 
            "barcodeNumber" : "690225106542", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "India gate basmati rice", 
            "barcodeNumber" : "690225106993", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "India gate basmati brain metabolism booster", 
            "barcodeNumber" : "690225300483", 
            "barcodePrice" : NumberInt(155), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "socolor matrix hair colour cream", 
            "barcodeNumber" : "6955818220765", 
            "barcodePrice" : NumberInt(340), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "socolor matrix hair colour cream", 
            "barcodeNumber" : "6955818273754", 
            "barcodePrice" : NumberInt(265)
        }, 
        {
            "barcodeName" : "Mahaan ghee ", 
            "barcodeNumber" : "750343880844", 
            "barcodePrice" : NumberInt(111)
        }, 
        {
            "barcodeName" : "Mahaan agmark ghee", 
            "barcodeNumber" : "750343880851", 
            "barcodePrice" : NumberInt(251)
        }, 
        {
            "barcodeName" : "Mahaan ghee", 
            "barcodeNumber" : "750343880875", 
            "barcodePrice" : NumberInt(498), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Lotus whiteglow 3 in 1 cleansing skin whitening facial foam", 
            "barcodeNumber" : "806360290507", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lotus jojobawash", 
            "barcodeNumber" : "806360560808", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lotus whiteglow active skin whitening + oil control face wash", 
            "barcodeNumber" : "806360742501", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "ayur astringent", 
            "barcodeNumber" : "808042000152", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ayur Skin Toner", 
            "barcodeNumber" : "808042000190", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Caneen Olive pomace oil", 
            "barcodeNumber" : "8428653412100", 
            "barcodePrice" : NumberInt(550), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Iodex fast relief pain balm", 
            "barcodeNumber" : "89000014", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur gulabari premium rose water", 
            "barcodeNumber" : "89003121", 
            "barcodePrice" : NumberInt(14)
        }, 
        {
            "barcodeName" : "Iodex fast relief balm", 
            "barcodeNumber" : "89003978", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur pudin hara active", 
            "barcodeNumber" : "89003985", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash energizing lemon(50ml)", 
            "barcodeNumber" : "8901012188026", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash brightening berry(50ml)", 
            "barcodeNumber" : "8901012188057", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash brightening berry(100ml)", 
            "barcodeNumber" : "8901012188064", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash purifying apple(50ml)", 
            "barcodeNumber" : "8901012188088", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash purifying apple(100ml)", 
            "barcodeNumber" : "8901012188095", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear clear fairness face wash(40g)", 
            "barcodeNumber" : "8901012188101", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear clear fairness face wash(80g)", 
            "barcodeNumber" : "8901012188118", 
            "barcodePrice" : NumberInt(100), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear morning energy face wash energizing lemon (100ml)", 
            "barcodeNumber" : "8901012188217", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Clean&Clear natural bright face wash (100ml)", 
            "barcodeNumber" : "8901012189115", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Goorej nupur henna", 
            "barcodeNumber" : "8901023006821", 
            "barcodePrice" : NumberInt(190)
        }, 
        {
            "barcodeName" : "godrej nupur henna for silky shiny hair", 
            "barcodeNumber" : "8901023007668", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit anti roach gel", 
            "barcodeNumber" : "8901023010002", 
            "barcodePrice" : NumberInt(175), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "godrej expert crème hair colour", 
            "barcodeNumber" : "8901023010330", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Good knight fast card mosquito card ", 
            "barcodeNumber" : "8901023011276", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for mosquitoes and flies spray", 
            "barcodeNumber" : "8901023014284", 
            "barcodePrice" : NumberInt(94), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for mosquitoes and flies spray", 
            "barcodeNumber" : "8901023014291", 
            "barcodePrice" : NumberInt(176), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for mosquitoes and flies spray", 
            "barcodeNumber" : "8901023014321", 
            "barcodePrice" : NumberInt(255), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Good knight cool gel", 
            "barcodeNumber" : "8901023014994", 
            "barcodePrice" : NumberInt(20)
        }, 
        {
            "barcodeName" : "Hit gel stick", 
            "barcodeNumber" : "8901023015175", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015335", 
            "barcodePrice" : NumberInt(199)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015342", 
            "barcodePrice" : NumberInt(185)
        }, 
        {
            "barcodeName" : "Bblunt salo secret high shine creme hair colour", 
            "barcodeNumber" : "8901023015359", 
            "barcodePrice" : NumberInt(185), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015373", 
            "barcodePrice" : NumberInt(199)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015946", 
            "barcodePrice" : NumberInt(85)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015953", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023015977", 
            "barcodePrice" : NumberInt(89)
        }, 
        {
            "barcodeName" : "Godrej qer fresh lush green", 
            "barcodeNumber" : "8901023016011", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Bblunt salon secret high shine crème hair colour", 
            "barcodeNumber" : "8901023016851", 
            "barcodePrice" : NumberInt(89)
        }, 
        {
            "barcodeName" : "Good knight green shakti low smoke coil", 
            "barcodeNumber" : "8901023017254", 
            "barcodePrice" : NumberInt(33), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Pears fresh renewal face wash", 
            "barcodeNumber" : "8901030355431", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pears pure and gentle face wash", 
            "barcodeNumber" : "8901030355448", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pears oil clear glow face wash", 
            "barcodeNumber" : "8901030355455", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pond's men energy charge face wash(50g)", 
            "barcodeNumber" : "8901030505508", 
            "barcodePrice" : NumberInt(95)
        }, 
        {
            "barcodeName" : "Pond's men energy charge face wash(100g)", 
            "barcodeNumber" : "8901030505515", 
            "barcodePrice" : NumberInt(180), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "pond's white beauty pearl cleansing gel", 
            "barcodeNumber" : "8901030537936", 
            "barcodePrice" : NumberInt(190), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pond's men pollution out deep clen face wash", 
            "barcodeNumber" : "8901030547720", 
            "barcodePrice" : NumberInt(105), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lakme blush & gliw strawberry gel face wash(50g)", 
            "barcodeNumber" : "8901030588822", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lakme blush & glow strawberry face wash", 
            "barcodeNumber" : "8901030588839", 
            "barcodePrice" : NumberInt(190), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lakme blush & glow peach gel face wash", 
            "barcodeNumber" : "8901030589911", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "ponds white beauty spotless fairness face wash", 
            "barcodeNumber" : "8901030591389", 
            "barcodePrice" : NumberInt(28), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "fair and lovely fairness face wash pollution clean up", 
            "barcodeNumber" : "8901030594199", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lifeboy immunity boosting hand sanitizer lemon fresh", 
            "barcodeNumber" : "8901030599187", 
            "barcodePrice" : NumberInt(69)
        }, 
        {
            "barcodeName" : "Lifebuoy immunity boosting hand sanitizer ", 
            "barcodeNumber" : "8901030599217", 
            "barcodePrice" : NumberInt(69), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Citra pearl fair gel face wash korean pink pearl(50g)", 
            "barcodeNumber" : "8901030621369", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Citra pearl fair gel face wash korean pink pearl(100g)", 
            "barcodeNumber" : "8901030621376", 
            "barcodePrice" : NumberInt(160), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Citra pimple clear face wash Japanese green tea(50g)", 
            "barcodeNumber" : "8901030622472", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Citra pimple clear face wash Japanese green tea(100g)", 
            "barcodeNumber" : "8901030622489", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Lakme absolute perfect radiance", 
            "barcodeNumber" : "8901030644870", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "lakme blush & glow lemon gel face wash", 
            "barcodeNumber" : "8901030668920", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "pond's pure white anti pollution+purity face wash", 
            "barcodeNumber" : "8901030681363", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Men's fair and lovely instant fairness rapid action face wash(20g)", 
            "barcodeNumber" : "8901030691195", 
            "barcodePrice" : NumberInt(35), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Men's fair and lovely instant fairness rapid action face wash(50g)", 
            "barcodeNumber" : "8901030691201", 
            "barcodePrice" : NumberInt(83), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "fair and lovely fairness face wash instant glow clean up", 
            "barcodeNumber" : "8901030691416", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Maggi 2 minute noodles", 
            "barcodeNumber" : "8901058851489", 
            "barcodePrice" : NumberInt(128), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Britannia little hearts classic", 
            "barcodeNumber" : "8901063019027", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "treat jimjam", 
            "barcodeNumber" : "8901063029231", 
            "barcodePrice" : NumberInt(10)
        }, 
        {
            "barcodeName" : "Britannia ghee danedar", 
            "barcodeNumber" : "8901063405332", 
            "barcodePrice" : NumberInt(525), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Britannia ghee", 
            "barcodeNumber" : "8901063405356", 
            "barcodePrice" : NumberInt(560), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "saffola gold edible vegetable oil", 
            "barcodeNumber" : "8901088017381", 
            "barcodePrice" : NumberInt(150)
        }, 
        {
            "barcodeName" : "Saffola active edible vegetable oil", 
            "barcodeNumber" : "8901088034593", 
            "barcodePrice" : NumberInt(130)
        }, 
        {
            "barcodeName" : "everyuth naturals rejuvenating Cucumber and aloe vere face pack ", 
            "barcodeNumber" : "8901120140831", 
            "barcodePrice" : NumberInt(60)
        }, 
        {
            "barcodeName" : "everyuth brightening lemon and cherry face wash(100g)", 
            "barcodeNumber" : "8901120141227", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "sugar free natura", 
            "barcodeNumber" : "8901120143115", 
            "barcodePrice" : NumberInt(65)
        }, 
        {
            "barcodeName" : "everyuth neem face wash(50g)", 
            "barcodeNumber" : "8901120143528", 
            "barcodePrice" : NumberInt(52), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Sugar free ", 
            "barcodeNumber" : "8901120143726", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "everyuth moisturizing fruit face wash(50g)", 
            "barcodeNumber" : "8901120146819", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "everyuth moisturizing fruit face wash(100g)", 
            "barcodeNumber" : "8901120146826", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya moisturizing aloe vera face wash(100ml)", 
            "barcodeNumber" : "8901138505530", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya lemon face wash", 
            "barcodeNumber" : "8901138509217", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya moisturizing aloe vera face wash(50ml)", 
            "barcodeNumber" : "8901138509224", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "himalaya Refreshing and clarifying Toner", 
            "barcodeNumber" : "8901138510329", 
            "barcodePrice" : NumberInt(83), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya gentle baby shampoo (100ml)", 
            "barcodeNumber" : "8901138511449", 
            "barcodePrice" : NumberInt(79), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya gentle baby shampoo (200ml)", 
            "barcodeNumber" : "8901138511456", 
            "barcodePrice" : NumberInt(149), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby lotion(100ml)", 
            "barcodeNumber" : "8901138511463", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby lotion", 
            "barcodeNumber" : "8901138511470", 
            "barcodePrice" : NumberInt(150), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby cream extra soft and gentle", 
            "barcodeNumber" : "8901138511494", 
            "barcodePrice" : NumberInt(121), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby massage oil", 
            "barcodeNumber" : "8901138511739", 
            "barcodePrice" : NumberInt(88), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby powder", 
            "barcodeNumber" : "8901138511814", 
            "barcodePrice" : NumberInt(63), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya purifying neem face wash(100ml)", 
            "barcodeNumber" : "8901138512460", 
            "barcodePrice" : NumberInt(117)
        }, 
        {
            "barcodeName" : "Himalaya neem foaming face wash (150ml)", 
            "barcodeNumber" : "8901138512811", 
            "barcodePrice" : NumberInt(195), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya Apricot face wash (100ml)", 
            "barcodeNumber" : "8901138712181", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya Apricot Face Wash(50ml)", 
            "barcodeNumber" : "8901138712198", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "himalaya under eye cream", 
            "barcodeNumber" : "8901138712235", 
            "barcodePrice" : NumberInt(165), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya purifying neem face wash(150ml)", 
            "barcodeNumber" : "8901138815431", 
            "barcodePrice" : NumberInt(150), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "himalaya age defying hand cream", 
            "barcodeNumber" : "890113881575", 
            "barcodePrice" : NumberInt(160), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya fairness kesar face wash(100ml)", 
            "barcodeNumber" : "8901138819668", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya fairness kesar face wash (50ml)", 
            "barcodeNumber" : "8901138819675", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya diaper rash cream", 
            "barcodeNumber" : "8901138819712", 
            "barcodePrice" : NumberInt(94), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya clear compelxion whitening face wash(100ml)", 
            "barcodeNumber" : "8901138821234", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya purifying neem pack face wash ", 
            "barcodeNumber" : "8901138821845", 
            "barcodePrice" : NumberInt(75)
        }, 
        {
            "barcodeName" : "Himalaya purifying neem pack", 
            "barcodeNumber" : "8901138821852", 
            "barcodePrice" : NumberInt(135)
        }, 
        {
            "barcodeName" : "Himalaya refreshing fruit pack", 
            "barcodeNumber" : "8901138821869", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Himalaya refreshing fruit pack", 
            "barcodeNumber" : "8901138821876", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Himalaya fairness kesar face pack", 
            "barcodeNumber" : "8901138821906", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Himalaya oil clear mud face wash", 
            "barcodeNumber" : "8901138821951", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Himalaya oil clean mud face pack", 
            "barcodeNumber" : "8901138821968", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Himalaya clear complexion whitening face wash(50ml)", 
            "barcodeNumber" : "8901138822286", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya neem foaming face wash(50ml)", 
            "barcodeNumber" : "8901138822460", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya neem face wash(200ml)", 
            "barcodeNumber" : "8901138822477", 
            "barcodePrice" : NumberInt(170), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby powder (400g)", 
            "barcodeNumber" : "8901138824037", 
            "barcodePrice" : NumberInt(176), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby massage oil", 
            "barcodeNumber" : "8901138829124", 
            "barcodePrice" : NumberInt(46), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya baby cream extra soft and gentle (200ml)", 
            "barcodeNumber" : "8901138831578", 
            "barcodePrice" : NumberInt(225), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya prickly heat baby Powder", 
            "barcodeNumber" : "8901138831745", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya tan removal orange face wash(100ml)", 
            "barcodeNumber" : "8901138837044", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya tan removal orange face wash(50ml)", 
            "barcodeNumber" : "8901138837051", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya intimate wash for moms", 
            "barcodeNumber" : "8901138837778", 
            "barcodePrice" : NumberInt(220), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya intimate wash for moms", 
            "barcodeNumber" : "8901138838065", 
            "barcodePrice" : NumberInt(116), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya extra moisturizing baby wash", 
            "barcodeNumber" : "8901138839000", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya extra moisturising baby soap", 
            "barcodeNumber" : "8901138839529", 
            "barcodePrice" : NumberInt(100), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya fresh start oil clear face wash strawberry (100ml)", 
            "barcodeNumber" : "8901138839659", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya fresh start oil clear face wash peach(100ml)", 
            "barcodeNumber" : "8901138839666", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Himalaya fresh start oil clear face wash lemon (100ml)", 
            "barcodeNumber" : "8901138839673", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Good knight mini jumbo", 
            "barcodeNumber" : "8901157004281", 
            "barcodePrice" : NumberInt(26), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for mosquitoes and flies spray", 
            "barcodeNumber" : "8901157025019", 
            "barcodePrice" : NumberInt(149), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for hidden cockroach", 
            "barcodeNumber" : "8901157025057", 
            "barcodePrice" : NumberInt(149), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Hit for mosquitoes and flies spray", 
            "barcodeNumber" : "8901157025194", 
            "barcodePrice" : NumberInt(255), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Godrej aer click gel fresh", 
            "barcodeNumber" : "8901157045017", 
            "barcodePrice" : NumberInt(279), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Godrej aer click gel cool", 
            "barcodeNumber" : "8901157045024", 
            "barcodePrice" : NumberInt(279), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "moov", 
            "barcodeNumber" : "8901177100505", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur pudin hara active", 
            "barcodeNumber" : "8901207006845", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur sat isabgol", 
            "barcodeNumber" : "8901207006852", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur sat isabgol(100g)", 
            "barcodeNumber" : "8901207006869", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dabur odomos mosquito repellent wrist band", 
            "barcodeNumber" : "8901207019203", 
            "barcodePrice" : NumberInt(199), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odonil natural ", 
            "barcodeNumber" : "8901207022296", 
            "barcodePrice" : NumberInt(49), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odonil natural air freshener green apple", 
            "barcodeNumber" : "8901207022692", 
            "barcodePrice" : NumberInt(129), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "odonil natural air freshener", 
            "barcodeNumber" : "8901207022708", 
            "barcodePrice" : NumberInt(204), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odomos cream ", 
            "barcodeNumber" : "8901207500039", 
            "barcodePrice" : NumberInt(25), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odomos mosquito repellent cream", 
            "barcodeNumber" : "8901207500046", 
            "barcodePrice" : NumberInt(44), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odonil natual ", 
            "barcodeNumber" : "8901207503023", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "odonil natural air freshener", 
            "barcodeNumber" : "8901207503566", 
            "barcodePrice" : NumberInt(201), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Odonil natural room freshener", 
            "barcodeNumber" : "8901207503887", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Kama sutra desire series dotted condoms", 
            "barcodeNumber" : "8901216406346", 
            "barcodePrice" : NumberInt(100)
        }, 
        {
            "barcodeName" : " Cadbury oreo", 
            "barcodeNumber" : "8901233025155", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Streax cream hair colour ", 
            "barcodeNumber" : "8901247577831", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "streax cream hair colour", 
            "barcodeNumber" : "8901247577848", 
            "barcodePrice" : NumberInt(28)
        }, 
        {
            "barcodeName" : "Streax cream hair colour", 
            "barcodeNumber" : "8901247577879", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "himani fast relief", 
            "barcodeNumber" : "8901248114226", 
            "barcodePrice" : NumberInt(12), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "himani fast relief ", 
            "barcodeNumber" : "8901248114233", 
            "barcodePrice" : NumberInt(58), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "himani fast relief", 
            "barcodeNumber" : "8901248114240", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Boro plus aloe vera coconut moisturising face wash", 
            "barcodeNumber" : "8901248137140", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Emami diamond shine crème hair colour", 
            "barcodeNumber" : "8901248257350", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Emami fair and handsome (20g)", 
            "barcodeNumber" : "8901248295024", 
            "barcodePrice" : NumberInt(38), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Emami fair and handsome instant fairness face wash", 
            "barcodeNumber" : "8901248295031", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Emami fair and handsome 100% oil clear instant fairness cream", 
            "barcodeNumber" : "8901248295147", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "zandu balm", 
            "barcodeNumber" : "8901248701105", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "zandu ultra power balm", 
            "barcodeNumber" : "8901248701129", 
            "barcodePrice" : NumberInt(35), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "zandu Nityam Tablet", 
            "barcodeNumber" : "8901248705042", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "zandu gel", 
            "barcodeNumber" : "8901248751001", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Amul pure ghee", 
            "barcodeNumber" : "8901262030069", 
            "barcodePrice" : NumberInt(485), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Amul pure ghee", 
            "barcodeNumber" : "8901262030175", 
            "barcodePrice" : NumberInt(2375), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Amul cow ghee", 
            "barcodeNumber" : "8901262030243", 
            "barcodePrice" : NumberInt(500)
        }, 
        {
            "barcodeName" : "Amul pure ghee ", 
            "barcodeNumber" : "8901262030250", 
            "barcodePrice" : NumberInt(250), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Amul pure ghee", 
            "barcodeNumber" : "8901262030267", 
            "barcodePrice" : NumberInt(255), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Amul cow ghee", 
            "barcodeNumber" : "8901262030519", 
            "barcodePrice" : NumberInt(242)
        }, 
        {
            "barcodeName" : "Amul pure ghee", 
            "barcodeNumber" : "8901262030588", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Premium lavender room freshener", 
            "barcodeNumber" : "8901277012470", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Premium sandal room freshener", 
            "barcodeNumber" : "8901277012487", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Premium Rajnigandha room freshener", 
            "barcodeNumber" : "8901277012494", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "premium the art of fragrance the rose", 
            "barcodeNumber" : "8901277012616", 
            "barcodePrice" : NumberInt(125)
        }, 
        {
            "barcodeName" : "Premium lemon room freshener", 
            "barcodeNumber" : "8901277015129", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Dettol instant hand sanitizer", 
            "barcodeNumber" : "8901396341901", 
            "barcodePrice" : NumberInt(35), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Dettol instant hand sanitizer", 
            "barcodeNumber" : "8901396348900", 
            "barcodePrice" : NumberInt(80)
        }, 
        {
            "barcodeName" : "Mortein power booster", 
            "barcodeNumber" : "8901396511007", 
            "barcodePrice" : NumberInt(32), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mortein insta", 
            "barcodeNumber" : "8901396512127", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mortein insta kills dengue mosquito", 
            "barcodeNumber" : "8901396512325", 
            "barcodePrice" : NumberInt(165), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mortein insta kills dengue mosquito", 
            "barcodeNumber" : "8901396512523", 
            "barcodePrice" : NumberInt(249), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mortein insta mosquito", 
            "barcodeNumber" : "8901396523505", 
            "barcodePrice" : NumberInt(78), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mortein insta", 
            "barcodeNumber" : "8901396523604", 
            "barcodePrice" : NumberInt(69), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Pour home room freshener", 
            "barcodeNumber" : "8901450000539", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Loreal paris excellence creme triple care colour", 
            "barcodeNumber" : "8901526100545", 
            "barcodePrice" : NumberInt(600), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Excellence triple care colour ", 
            "barcodeNumber" : "8901526100569", 
            "barcodePrice" : NumberInt(590)
        }, 
        {
            "barcodeName" : "Loreal paris casting crème gloss conditioning colour", 
            "barcodeNumber" : "8901526101016", 
            "barcodePrice" : NumberInt(550)
        }, 
        {
            "barcodeName" : "Casting crème gloss conditioning colour", 
            "barcodeNumber" : "8901526101023", 
            "barcodePrice" : NumberInt(550)
        }, 
        {
            "barcodeName" : "L'Oréal Paris excellence creme triple care colour ", 
            "barcodeNumber" : "8901526101122", 
            "barcodePrice" : NumberInt(590)
        }, 
        {
            "barcodeName" : "L'Oréal Paris excellence creme triple hair colour", 
            "barcodeNumber" : "8901526104253", 
            "barcodePrice" : NumberInt(199)
        }, 
        {
            "barcodeName" : "L'Oréal Paris casting creme gloss conditioning colour", 
            "barcodeNumber" : "8901526105786", 
            "barcodePrice" : NumberInt(199)
        }, 
        {
            "barcodeName" : "L'Oréal Paris casting crème b gloss", 
            "barcodeNumber" : "8901526105793", 
            "barcodePrice" : NumberInt(199)
        }, 
        {
            "barcodeName" : "Loreal casting creame gloss conditioning colour", 
            "barcodeNumber" : "8901526105809", 
            "barcodePrice" : NumberInt(299)
        }, 
        {
            "barcodeName" : "Garnier skin naturals white complete airness face wash ", 
            "barcodeNumber" : "8901526204229", 
            "barcodePrice" : NumberInt(82), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing permanent hair color", 
            "barcodeNumber" : "8901526204465", 
            "barcodePrice" : NumberInt(175)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing permanent hair color", 
            "barcodeNumber" : "8901526204472", 
            "barcodePrice" : NumberInt(175), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing permanent hair color", 
            "barcodeNumber" : "8901526204489", 
            "barcodePrice" : NumberInt(175)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing permanent hair color", 
            "barcodeNumber" : "8901526204496", 
            "barcodePrice" : NumberInt(175)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing permanent hair color", 
            "barcodeNumber" : "8901526204748", 
            "barcodePrice" : NumberInt(80)
        }, 
        {
            "barcodeName" : "Garnier color naturals nourishing", 
            "barcodeNumber" : "8901526206377", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Garnier pure active face wash", 
            "barcodeNumber" : "8901526207480", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Garnier gentle smoothing face wash", 
            "barcodeNumber" : "8901526209569", 
            "barcodePrice" : NumberInt(47), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Garnier white complete double action face wash", 
            "barcodeNumber" : "8901526212224", 
            "barcodePrice" : NumberInt(170), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Matrix 20 vol creme oxydant", 
            "barcodeNumber" : "8901526403608", 
            "barcodePrice" : NumberInt(390)
        }, 
        {
            "barcodeName" : "Matrix 30 vol creme oxydant", 
            "barcodeNumber" : "8901526403615", 
            "barcodePrice" : NumberInt(390)
        }, 
        {
            "barcodeName" : "Matrix 40 vol creme oxydant", 
            "barcodeNumber" : "8901526403622", 
            "barcodePrice" : NumberInt(410), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "socolor matrix hair colour cream", 
            "barcodeNumber" : "8901526404179", 
            "barcodePrice" : NumberInt(275)
        }, 
        {
            "barcodeName" : "Garnier light complete fairness face wash", 
            "barcodeNumber" : "8901526530274", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Heritage basmati rice premium", 
            "barcodeNumber" : "8901537004030", 
            "barcodePrice" : NumberInt(514)
        }, 
        {
            "barcodeName" : "Heritage basmati rice classic gold", 
            "barcodeNumber" : "8901537004290", 
            "barcodePrice" : NumberInt(499), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Heritage basmati rice classic gold", 
            "barcodeNumber" : "8901537004351", 
            "barcodePrice" : NumberInt(1275), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Heritage basmati rice", 
            "barcodeNumber" : "8901537004382", 
            "barcodePrice" : NumberInt(149)
        }, 
        {
            "barcodeName" : "Heritage basmati rice", 
            "barcodeNumber" : "8901537004788", 
            "barcodePrice" : NumberInt(149), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Daawat rosana basmati rice", 
            "barcodeNumber" : "8901537006010", 
            "barcodePrice" : NumberInt(99)
        }, 
        {
            "barcodeName" : "Daawat rozana basmati rice", 
            "barcodeNumber" : "8901537006027", 
            "barcodePrice" : NumberInt(495), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Daawat rozana basmati rice super", 
            "barcodeNumber" : "8901537007116", 
            "barcodePrice" : NumberInt(369)
        }, 
        {
            "barcodeName" : "Daawat rozana basmati rice", 
            "barcodeNumber" : "8901537007123", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Daawat rozana basmati rice gini", 
            "barcodeNumber" : "8901537021563", 
            "barcodePrice" : NumberInt(711)
        }, 
        {
            "barcodeName" : "Daawat super basmati rice", 
            "barcodeNumber" : "8901537025127", 
            "barcodePrice" : NumberInt(165), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Daawat super basmati rice", 
            "barcodeNumber" : "8901537025134", 
            "barcodePrice" : NumberInt(800)
        }, 
        {
            "barcodeName" : "Everyuth naturals neem face pack", 
            "barcodeNumber" : "8901548146729", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "everyuth tulsi tumeric face wash(50g)", 
            "barcodeNumber" : "8901548146767", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "everyuth tulsi tumeric face wash(100g)", 
            "barcodeNumber" : "8901548146774", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "everyuth brightening leman and cherry face wash(50g)", 
            "barcodeNumber" : "8901548147436", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Sugar free green veda tulsi", 
            "barcodeNumber" : "8901548431122", 
            "barcodePrice" : NumberInt(99)
        }, 
        {
            "barcodeName" : "Nilon's panner chili maamla", 
            "barcodeNumber" : "8901560614541", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nilons gold mustard oil", 
            "barcodeNumber" : "8901560800517", 
            "barcodePrice" : NumberInt(85)
        }, 
        {
            "barcodeName" : "Chings secret schezwan fried rice masala ", 
            "barcodeNumber" : "8901595972111", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Mother dairy pure healthy ghee", 
            "barcodeNumber" : "8901648094746", 
            "barcodePrice" : NumberInt(510), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Parle hide seek biscuits", 
            "barcodeNumber" : "8901719100369", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Parle krack jack", 
            "barcodeNumber" : "8901719100710", 
            "barcodePrice" : NumberInt(25), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Boro plus zero oil zero pimple duo face wash", 
            "barcodeNumber" : "8901842137126", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Maxo a grade", 
            "barcodeNumber" : "8902102197508", 
            "barcodePrice" : NumberInt(26), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Maxo a grade fist all machines", 
            "barcodeNumber" : "8902102197522", 
            "barcodePrice" : NumberInt(67), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Ramedu gold compounded hing", 
            "barcodeNumber" : "8902188814054", 
            "barcodePrice" : NumberInt(160)
        }, 
        {
            "barcodeName" : "Ramedu gold compunded hing", 
            "barcodeNumber" : "8902188814061", 
            "barcodePrice" : NumberInt(210)
        }, 
        {
            "barcodeName" : "Patanjali digestive cookies", 
            "barcodeNumber" : "8902351222402", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Ozone sandal face wash", 
            "barcodeNumber" : "8902443500791", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ozone acne check face wash", 
            "barcodeNumber" : "8902443501354", 
            "barcodePrice" : NumberInt(210), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ozone complexion brightening face wash", 
            "barcodeNumber" : "8902443501385", 
            "barcodePrice" : NumberInt(210), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ozone henna conditioner", 
            "barcodeNumber" : "8902443501491", 
            "barcodePrice" : NumberInt(90)
        }, 
        {
            "barcodeName" : "Ozone neem face wash", 
            "barcodeNumber" : "8902443501750", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ozone aloe Vera face wash", 
            "barcodeNumber" : "8902443501927", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ozone whitening crème face wash", 
            "barcodeNumber" : "8902443502184", 
            "barcodePrice" : NumberInt(325), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Good home air freshener dreams of dew", 
            "barcodeNumber" : "8902618000620", 
            "barcodePrice" : NumberInt(165), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Indica herbal hair colour", 
            "barcodeNumber" : "8902979001953", 
            "barcodePrice" : NumberInt(17), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Indica easy hair colour shampoo based", 
            "barcodeNumber" : "8902979026093", 
            "barcodePrice" : NumberInt(40)
        }, 
        {
            "barcodeName" : "Indica shampoo based hair colour", 
            "barcodeNumber" : "8902979027144", 
            "barcodePrice" : NumberInt(20)
        }, 
        {
            "barcodeName" : "Lia car freshener aqua dream", 
            "barcodeNumber" : "8903664047478", 
            "barcodePrice" : NumberInt(250)
        }, 
        {
            "barcodeName" : "Lia car freshener citrus fresh", 
            "barcodeNumber" : "8903664047485", 
            "barcodePrice" : NumberInt(250), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Lia car freshener french lavender", 
            "barcodeNumber" : "8903664048093", 
            "barcodePrice" : NumberInt(250), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Stop-o stops odour english lavender", 
            "barcodeNumber" : "8903664048123", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Stop-o stops odour lemon grass", 
            "barcodeNumber" : "8903664048130", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "lia chandanam room spray", 
            "barcodeNumber" : "8903664048215", 
            "barcodePrice" : NumberInt(130), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Stop-o brick stops odour", 
            "barcodeNumber" : "8903664048291", 
            "barcodePrice" : NumberInt(120)
        }, 
        {
            "barcodeName" : "Lia lavender room freshener", 
            "barcodeNumber" : "8903664049984", 
            "barcodePrice" : NumberInt(140)
        }, 
        {
            "barcodeName" : "Lia lia fruitz room freshener", 
            "barcodeNumber" : "8903664049991", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Lia rose room freshener", 
            "barcodeNumber" : "8903664050003", 
            "barcodePrice" : NumberInt(140)
        }, 
        {
            "barcodeName" : "Lia sea shore room refreshener", 
            "barcodeNumber" : "8903664050010", 
            "barcodePrice" : NumberInt(140)
        }, 
        {
            "barcodeName" : "Lia lemon burst room refeshener", 
            "barcodeNumber" : "8903664050447", 
            "barcodePrice" : NumberInt(140)
        }, 
        {
            "barcodeName" : "Riddhi hing", 
            "barcodeNumber" : "8904018302038", 
            "barcodePrice" : NumberInt(170), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Milan mehandi", 
            "barcodeNumber" : "8904021700111", 
            "barcodePrice" : NumberInt(50)
        }, 
        {
            "barcodeName" : "Milan mehandi ", 
            "barcodeNumber" : "8904021788881", 
            "barcodePrice" : NumberInt(24), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Jungle magic hand sanitizer", 
            "barcodeNumber" : "8904026626881", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : " Naturolax Isapgol Husk powder", 
            "barcodeNumber" : "8904026631045", 
            "barcodePrice" : 85.69999694824219, 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Naturalax Isabgol Husk Powder", 
            "barcodeNumber" : "8904026631052", 
            "barcodePrice" : NumberInt(225), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "sloan's balm", 
            "barcodeNumber" : "8904026631908", 
            "barcodePrice" : NumberInt(54), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Ferradol food supplement", 
            "barcodeNumber" : "8904026632066", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "rosse rose water", 
            "barcodeNumber" : "8904029411149", 
            "barcodePrice" : NumberInt(40), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "rosse rose water", 
            "barcodeNumber" : "8904029412009", 
            "barcodePrice" : NumberInt(15), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "pacin coldoff balm", 
            "barcodeNumber" : "8904029412047", 
            "barcodePrice" : NumberInt(10), 
            "barcodePricePkt" : NumberInt(80), 
            "barcodeStock" : NumberInt(2), 
            "barcodeStockPkt" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy keshar chandan natural fairness face pack", 
            "barcodeNumber" : "8904035413021", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "joy skin fruit fairness face wash", 
            "barcodeNumber" : "8904035416664", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy skin fruit gentle care face wash (100ml)", 
            "barcodeNumber" : "8904035416671", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy tumeric neem purifying face wash", 
            "barcodeNumber" : "8904035416749", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy skin care fairness fruit pack", 
            "barcodeNumber" : "8904035416909", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy pure neem face wash(50ml)", 
            "barcodeNumber" : "8904035417005", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy pure neem face wash (100ml)", 
            "barcodeNumber" : "8904035417012", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Joy sun sunblock anti tan lotion", 
            "barcodeNumber" : "8904035417111", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "joy skin fruit gentle care face wash(30ml)", 
            "barcodeNumber" : "8904035417500", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy skin fruit fairness face wash", 
            "barcodeNumber" : "8904035417517", 
            "barcodePrice" : NumberInt(30), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy pure neem face wash", 
            "barcodeNumber" : "8904035419313", 
            "barcodePrice" : NumberInt(15), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Joy sun  sunblock anti tan lotion", 
            "barcodeNumber" : "8904035420272", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "x men zest Body Deodrant", 
            "barcodeNumber" : "8904035420869", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "xmen charge body deodrant", 
            "barcodeNumber" : "8904035420876", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy keshar chandan face wash", 
            "barcodeNumber" : "8904035421057", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy neem and turmeric face wash", 
            "barcodeNumber" : "8904035421064", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy pure aloe face wash", 
            "barcodeNumber" : "8904035421071", 
            "barcodePrice" : NumberInt(20), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "joy Pure Aloe Repairing And Soothing Face and body gel", 
            "barcodeNumber" : "8904035421811", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Tata sampann urad dal", 
            "barcodeNumber" : "8904043926117", 
            "barcodePrice" : NumberInt(129)
        }, 
        {
            "barcodeName" : "Tata sampann urad dal", 
            "barcodeNumber" : "8904043926124", 
            "barcodePrice" : NumberInt(65)
        }, 
        {
            "barcodeName" : "Tata sampann toor dal", 
            "barcodeNumber" : "8904043926223", 
            "barcodePrice" : NumberInt(59)
        }, 
        {
            "barcodeName" : "Tata sampann moong dal", 
            "barcodeNumber" : "8904043926315", 
            "barcodePrice" : NumberInt(119)
        }, 
        {
            "barcodeName" : "Tata sampann moong dal", 
            "barcodeNumber" : "8904043926322", 
            "barcodePrice" : NumberInt(64)
        }, 
        {
            "barcodeName" : "Tata sampann moong chilka", 
            "barcodeNumber" : "8904043926520", 
            "barcodePrice" : NumberInt(61)
        }, 
        {
            "barcodeName" : "Tata sampann chana dal", 
            "barcodeNumber" : "890404392662", 
            "barcodePrice" : NumberInt(64)
        }, 
        {
            "barcodeName" : "Tata sampann chana dal", 
            "barcodeNumber" : "8904043926629", 
            "barcodePrice" : NumberInt(64)
        }, 
        {
            "barcodeName" : "Tata sampann masoor dal whole", 
            "barcodeNumber" : "8904043926650", 
            "barcodePrice" : NumberInt(109)
        }, 
        {
            "barcodeName" : "Tata sampann low oil absorb besan", 
            "barcodeNumber" : "8904043926797", 
            "barcodePrice" : NumberInt(115), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Tata sampann low oil absorb besan", 
            "barcodeNumber" : "8904043926803", 
            "barcodePrice" : NumberInt(64), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Vitro naturals aloe skin gel", 
            "barcodeNumber" : "8904045052852", 
            "barcodePrice" : NumberInt(75)
        }, 
        {
            "barcodeName" : "divya peedantak thaila", 
            "barcodeNumber" : "8904049100399", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Jiya neem mud pack", 
            "barcodeNumber" : "8904050601748", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Jiya kesar ubtan face pack", 
            "barcodeNumber" : "8904050601762", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Jiva neem face wash", 
            "barcodeNumber" : "8904050602967", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "jiva aloe mint face wash", 
            "barcodeNumber" : "8904050606378", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Neem & aloe mint face wash combo", 
            "barcodeNumber" : "8904050606873", 
            "barcodePrice" : NumberInt(175), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dr. batras face wash", 
            "barcodeNumber" : "8904050700731", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Dr batra's acne clear face wash", 
            "barcodeNumber" : "8904050700779", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dr.batras moisturizing face wash", 
            "barcodeNumber" : "8904050700786", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dr. batras instant glow face wash", 
            "barcodeNumber" : "8904050700793", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Dr. batras oil control face wash", 
            "barcodeNumber" : "8904050704012", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Herbal khatnil", 
            "barcodeNumber" : "8904058700054", 
            "barcodePrice" : NumberInt(110)
        }, 
        {
            "barcodeName" : "Herbal khatnil for all insects", 
            "barcodeNumber" : "8904058700078", 
            "barcodePrice" : NumberInt(180), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Laxmanrekhaa for cockroaches", 
            "barcodeNumber" : "8904058700375", 
            "barcodePrice" : NumberInt(15), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Riddhi premium compounded hing asafoetida", 
            "barcodeNumber" : "8904072308441", 
            "barcodePrice" : NumberInt(50)
        }, 
        {
            "barcodeName" : "patanjali soundarya coco body butter", 
            "barcodeNumber" : "8904109400780", 
            "barcodePrice" : NumberInt(425), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Patanjali soyabean oil", 
            "barcodeNumber" : "8904109401008", 
            "barcodePrice" : NumberInt(105)
        }, 
        {
            "barcodeName" : "patanjali compounded asafoetida", 
            "barcodeNumber" : "8904109445392", 
            "barcodePrice" : NumberInt(40)
        }, 
        {
            "barcodeName" : "Patanjali brown rice", 
            "barcodeNumber" : "8904109467981", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "ayur skin toner", 
            "barcodeNumber" : "8904135205908", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Mayuri henna ", 
            "barcodeNumber" : "8904242800010", 
            "barcodePrice" : NumberInt(25)
        }, 
        {
            "barcodeName" : "Mayuri henna", 
            "barcodeNumber" : "8904242800034", 
            "barcodePrice" : NumberInt(10)
        }, 
        {
            "barcodeName" : "Kohinoor brown basmati rice", 
            "barcodeNumber" : "8904250700111", 
            "barcodePrice" : NumberInt(169), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Trophy royale basmati rice", 
            "barcodeNumber" : "8904250700531", 
            "barcodePrice" : NumberInt(129), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nivea refreshing face wash", 
            "barcodeNumber" : "8904256000208", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nivea face wash", 
            "barcodeNumber" : "8904256000239", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Dhara filtered groundnut oil", 
            "barcodeNumber" : "8906004620157", 
            "barcodePrice" : NumberInt(168)
        }, 
        {
            "barcodeName" : "Dhara kachi ghani mustard oil", 
            "barcodeNumber" : "8906004620225", 
            "barcodePrice" : NumberInt(342), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Milkfood dasi ghee ", 
            "barcodeNumber" : "8906004970016", 
            "barcodePrice" : NumberInt(245), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Milkfood dasi ghee ", 
            "barcodeNumber" : "8906004970023", 
            "barcodePrice" : NumberInt(450), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "All out super", 
            "barcodeNumber" : "8906006430273", 
            "barcodePrice" : NumberInt(81)
        }, 
        {
            "barcodeName" : "All out fight dengue ", 
            "barcodeNumber" : "8906006430419", 
            "barcodePrice" : NumberInt(72), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "All out anti dengue coil", 
            "barcodeNumber" : "8906006432147", 
            "barcodePrice" : NumberInt(24), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "All out flash guard", 
            "barcodeNumber" : "8906006432222", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "All out multi insect killer 5 in1", 
            "barcodeNumber" : "8906006435520", 
            "barcodePrice" : NumberInt(72)
        }, 
        {
            "barcodeName" : "Fortune sunlite rfined sunflower oil", 
            "barcodeNumber" : "8906007280242", 
            "barcodePrice" : NumberInt(115)
        }, 
        {
            "barcodeName" : "Fortune rice bran health oil", 
            "barcodeNumber" : "8906007280693", 
            "barcodePrice" : NumberInt(120), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Fortune super basmati rice", 
            "barcodeNumber" : "8906007282475", 
            "barcodePrice" : NumberInt(160)
        }, 
        {
            "barcodeName" : "Fortune super basmati rice", 
            "barcodeNumber" : "8906007282482", 
            "barcodePrice" : NumberInt(790)
        }, 
        {
            "barcodeName" : "Fortune soya chunks ", 
            "barcodeNumber" : "8906007283144", 
            "barcodePrice" : NumberInt(45), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Fortune rozana basmati rice", 
            "barcodeNumber" : "8906007287883", 
            "barcodePrice" : NumberInt(105)
        }, 
        {
            "barcodeName" : "Fortune khichdi basmati rice", 
            "barcodeNumber" : "8906007288026", 
            "barcodePrice" : NumberInt(76), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Fortune chhota basmati rice", 
            "barcodeNumber" : "8906007288040", 
            "barcodePrice" : NumberInt(84)
        }, 
        {
            "barcodeName" : "Fortune sarso oil ", 
            "barcodeNumber" : "8906007288101", 
            "barcodePrice" : NumberInt(58)
        }, 
        {
            "barcodeName" : "VLCC melia face wash", 
            "barcodeNumber" : "8906008450750", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Vlcc Punarnava Astringent", 
            "barcodeNumber" : "8906008450798", 
            "barcodePrice" : NumberInt(16), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC wild tumeric face wash", 
            "barcodeNumber" : "8906008450804", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Vlcc snigdha skin whitening Face mask", 
            "barcodeNumber" : "8906008450842", 
            "barcodePrice" : NumberInt(155), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Vlcc Almond Under Eye Cream", 
            "barcodeNumber" : "8906008452846", 
            "barcodePrice" : NumberInt(195), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC Natural herbal henna", 
            "barcodeNumber" : "8906008460476", 
            "barcodePrice" : NumberInt(89), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Divya fresh liye kitchen", 
            "barcodeNumber" : "8906008881011", 
            "barcodePrice" : NumberInt(135), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Divya fresh lite kitchen special", 
            "barcodeNumber" : "8906008881028", 
            "barcodePrice" : NumberInt(55)
        }, 
        {
            "barcodeName" : "Pure Roots Skin Toner", 
            "barcodeNumber" : "8906008986211", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(2)
        }, 
        {
            "barcodeName" : "pure Roots Astringent", 
            "barcodeNumber" : "8906008987119", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pure roots rose face wash", 
            "barcodeNumber" : "8906008987478", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pure roots gold face wash", 
            "barcodeNumber" : "8906008987966", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Pure roots acne probe face wash", 
            "barcodeNumber" : "8906008988161", 
            "barcodePrice" : NumberInt(50)
        }, 
        {
            "barcodeName" : "sulphurfree sugar", 
            "barcodeNumber" : "8906009620039", 
            "barcodePrice" : NumberInt(60)
        }, 
        {
            "barcodeName" : "Doctor brand naphthalene balls", 
            "barcodeNumber" : "8906012040121", 
            "barcodePrice" : NumberInt(35)
        }, 
        {
            "barcodeName" : "Valinita skin whitening face wash", 
            "barcodeNumber" : "8906012110329", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Valinita lemon face wash", 
            "barcodeNumber" : "8906012110343", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Valinita neem face wash", 
            "barcodeNumber" : "8906012110350", 
            "barcodePrice" : NumberInt(50), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Gajanand compounded asafoetida", 
            "barcodeNumber" : "8906012570253", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Taaza spices rock salt", 
            "barcodeNumber" : "8906013770775", 
            "barcodePrice" : NumberInt(15)
        }, 
        {
            "barcodeName" : "Nisha color perfect crème hair colour", 
            "barcodeNumber" : "8906015580600", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Nisha natural henna based hair colour", 
            "barcodeNumber" : "8906015582413", 
            "barcodePrice" : NumberInt(10)
        }, 
        {
            "barcodeName" : "Color mate hair color creme", 
            "barcodeNumber" : "8906016050256", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Color mate hair color creme", 
            "barcodeNumber" : "8906016050263", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Color mate hair color creme", 
            "barcodeNumber" : "8906016050294", 
            "barcodePrice" : NumberInt(90), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "color mate silky ceme hair color", 
            "barcodeNumber" : "8906016051628", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Ammbar groundnut oil", 
            "barcodeNumber" : "8906019320080", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Engine agmark kachi ghani mustard oil", 
            "barcodeNumber" : "8906020930100", 
            "barcodePrice" : NumberInt(70)
        }, 
        {
            "barcodeName" : "Engine til oil ", 
            "barcodeNumber" : "8906020931121", 
            "barcodePrice" : NumberInt(60)
        }, 
        {
            "barcodeName" : "upasana kachi ghani mustard oil", 
            "barcodeNumber" : "8906020933064", 
            "barcodePrice" : NumberInt(134)
        }, 
        {
            "barcodeName" : "Upasana kachi ghani mustard oil", 
            "barcodeNumber" : "8906020933071", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Nok lines  for cockroach ants", 
            "barcodeNumber" : "8906021590068", 
            "barcodePrice" : NumberInt(15), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Assure sun defense spf 30 plus", 
            "barcodeNumber" : "8906031311677", 
            "barcodePrice" : NumberInt(240), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "TBC organic defense neem & aloevera face wash", 
            "barcodeNumber" : "8906035313110", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC real basil oil control basil face wash", 
            "barcodeNumber" : "8906035314353", 
            "barcodePrice" : NumberInt(80), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC diamond perfect forever maximum radiance whitening exfoliating face wash", 
            "barcodeNumber" : "8906035314667", 
            "barcodePrice" : NumberInt(95), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC Almond And Pistchio Under Eye Cream", 
            "barcodeNumber" : "8906035315053", 
            "barcodePrice" : NumberInt(165), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC ultimate strawberry fairness scrub wash ", 
            "barcodeNumber" : "8906035315107", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC 24ct gold perfect glow instant glow face wash", 
            "barcodeNumber" : "8906035315503", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC foot cream", 
            "barcodeNumber" : "8906035318450", 
            "barcodePrice" : NumberInt(110), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC organic protection power D tan++ sun protective face wash", 
            "barcodeNumber" : "8906035318511", 
            "barcodePrice" : NumberInt(70), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "TBC luxury face wash", 
            "barcodeNumber" : "8906035318689", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "nature's essence purifying neem & aloe Vera face wash", 
            "barcodeNumber" : "8906045490948", 
            "barcodePrice" : NumberInt(60), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Nature's essence gold illuminating face wash", 
            "barcodeNumber" : "8906045491020", 
            "barcodePrice" : NumberInt(60)
        }, 
        {
            "barcodeName" : "Nature's essence perfect papaya depigmentation face wash", 
            "barcodeNumber" : "8906045492034", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Disano olive performance oil", 
            "barcodeNumber" : "8906047522364", 
            "barcodePrice" : NumberInt(375)
        }, 
        {
            "barcodeName" : "Gaia olive oil extra light", 
            "barcodeNumber" : "8906058610098", 
            "barcodePrice" : NumberInt(690)
        }, 
        {
            "barcodeName" : "Pooja naturals black salt powder", 
            "barcodeNumber" : "8906071360451", 
            "barcodePrice" : NumberInt(60)
        }, 
        {
            "barcodeName" : "Flowerom fantasia air freshener", 
            "barcodeNumber" : "8906072510008", 
            "barcodePrice" : NumberInt(130)
        }, 
        {
            "barcodeName" : "Meglow fairness. face wash", 
            "barcodeNumber" : "8906078000107", 
            "barcodePrice" : NumberInt(85), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "soft siles intensive foot care cream", 
            "barcodeNumber" : "8906078000558", 
            "barcodePrice" : NumberInt(65), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Luvit chocopops", 
            "barcodeNumber" : "8906079010402", 
            "barcodePrice" : NumberInt(5)
        }, 
        {
            "barcodeName" : "Dnd aeromix coil diffuser", 
            "barcodeNumber" : "8906079015018", 
            "barcodePrice" : NumberInt(249), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Oxy oil control active face wash", 
            "barcodeNumber" : "8906085380117", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Oxy whitening peel face wash", 
            "barcodeNumber" : "8906085380216", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Oxy v charge scrub face wash", 
            "barcodeNumber" : "8906085380315", 
            "barcodePrice" : NumberInt(99)
        }, 
        {
            "barcodeName" : "Acnes clarifying face wash", 
            "barcodeNumber" : "8906085380513", 
            "barcodePrice" : NumberInt(99), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "aroma leaf orgplus pearl fairness face wash", 
            "barcodeNumber" : "8906091730067", 
            "barcodePrice" : NumberInt(195), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "aroma leaf 24ct gold radiancr face wash", 
            "barcodeNumber" : "8906091730074", 
            "barcodePrice" : NumberInt(195), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "aroma leaf D-Tan tan removal face wash", 
            "barcodeNumber" : "8906091730081", 
            "barcodePrice" : NumberInt(245), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "orgplus papaya exfoliating pack", 
            "barcodeNumber" : "8906091730166", 
            "barcodePrice" : NumberInt(195)
        }, 
        {
            "barcodeName" : "Orgplus d tan tan removal pack", 
            "barcodeNumber" : "8906091730197", 
            "barcodePrice" : NumberInt(245), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "VLCC neem face wash(150ml)", 
            "barcodeNumber" : "8907122002641", 
            "barcodePrice" : NumberInt(80), 
            "barcodePricePkt" : NumberInt(150), 
            "barcodeStock" : NumberInt(1), 
            "barcodeStockPkt" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC mulberry & rose fairness face wash", 
            "barcodeNumber" : "8907122002658", 
            "barcodePrice" : NumberInt(80), 
            "barcodePricePkt" : NumberInt(150), 
            "barcodeStock" : NumberInt(1), 
            "barcodeStockPkt" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC tumeric & berberis facr wash", 
            "barcodeNumber" : "8907122002665", 
            "barcodePrice" : NumberInt(80), 
            "barcodePricePkt" : NumberInt(150), 
            "barcodeStock" : NumberInt(1), 
            "barcodeStockPkt" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC snigdha skin whitening face wash", 
            "barcodeNumber" : "8907122003105", 
            "barcodePrice" : NumberInt(155), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC neem face wash(50ml)", 
            "barcodeNumber" : "8907122005413", 
            "barcodePrice" : NumberInt(49), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC Ayurveda haldi & tulsi face wash", 
            "barcodeNumber" : "8907122006069", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC Ayurveda double power double neem face wash", 
            "barcodeNumber" : "8907122006106", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "VLCC Ayurveda chandan & kesar face wash", 
            "barcodeNumber" : "8907122006120", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Msg soya power boost", 
            "barcodeNumber" : "8907434001202", 
            "barcodePrice" : NumberInt(10), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Ankur groundnut oil", 
            "barcodeNumber" : "8908000096042", 
            "barcodePrice" : NumberInt(285)
        }, 
        {
            "barcodeName" : "Max airfresh lavender", 
            "barcodeNumber" : "8908000432338", 
            "barcodePrice" : NumberInt(35), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Max airfresh rose", 
            "barcodeNumber" : "8908000432352", 
            "barcodePrice" : NumberInt(105)
        }, 
        {
            "barcodeName" : "Max airfresh jasmin", 
            "barcodeNumber" : "8908000432406", 
            "barcodePrice" : NumberInt(55), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Max airfresh perfume blocks rose", 
            "barcodeNumber" : "8908000432444", 
            "barcodePrice" : NumberInt(165)
        }, 
        {
            "barcodeName" : "Max airfresh combo pack of 6 fragrances", 
            "barcodeNumber" : "8908000432598", 
            "barcodePrice" : NumberInt(120)
        }, 
        {
            "barcodeName" : "Oleev active olive oil", 
            "barcodeNumber" : "8908000863460", 
            "barcodePrice" : NumberInt(190), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Baba cow ghee", 
            "barcodeNumber" : "8908000921443", 
            "barcodePrice" : NumberInt(240)
        }, 
        {
            "barcodeName" : "Next fresh rose vanilla premium air freshener", 
            "barcodeNumber" : "8908001434799", 
            "barcodePrice" : NumberInt(140), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Ayurvedic kaayam tablet", 
            "barcodeNumber" : "8908001948531", 
            "barcodePrice" : NumberInt(280), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Anjali aata", 
            "barcodeNumber" : "8908002434408", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Anjali bagar", 
            "barcodeNumber" : "8908002434477", 
            "barcodePrice" : NumberInt(30)
        }, 
        {
            "barcodeName" : "Globe superfine desiccated coconut powder", 
            "barcodeNumber" : "8908003199054", 
            "barcodePrice" : NumberInt(300)
        }, 
        {
            "barcodeName" : "Aroe herbal face pack", 
            "barcodeNumber" : "8908003851495", 
            "barcodePrice" : NumberInt(90)
        }, 
        {
            "barcodeName" : "zhakaas masala moongodi", 
            "barcodeNumber" : "8908005103332", 
            "barcodePrice" : NumberInt(45)
        }, 
        {
            "barcodeName" : "Luvit crazy pops", 
            "barcodeNumber" : "8908005461104", 
            "barcodePrice" : NumberInt(5)
        }, 
        {
            "barcodeName" : "nature oure kachi ghani pure mustard oil", 
            "barcodeNumber" : "8908007043100", 
            "barcodePrice" : NumberInt(85)
        }, 
        {
            "barcodeName" : "superub pain relief gel", 
            "barcodeNumber" : "8908007611064", 
            "barcodePrice" : NumberInt(69), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Sadbhav methi", 
            "barcodeNumber" : "8908008396113", 
            "barcodePrice" : NumberInt(25), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Sadbhav aniseed", 
            "barcodeNumber" : "8908008396137", 
            "barcodePrice" : NumberInt(51), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Sadbhav aniseed ", 
            "barcodeNumber" : "8908008396144", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "sadbhav aniseed", 
            "barcodeNumber" : "8908008396205", 
            "barcodePrice" : NumberInt(27)
        }, 
        {
            "barcodeName" : "Jainism gagan brand", 
            "barcodeNumber" : "890946098082", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(0)
        }, 
        {
            "barcodeName" : "Vastu premium cow's ghee", 
            "barcodeNumber" : "8919913985226", 
            "barcodePrice" : NumberInt(520)
        }, 
        {
            "barcodeName" : "Tbc roselove hydrating toner", 
            "barcodeNumber" : "906035314391", 
            "barcodePrice" : NumberInt(145), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Aroe pigment lightning gel", 
            "barcodeNumber" : "RSM1101", 
            "barcodePrice" : NumberInt(125), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Aroe aloe vera skin gel", 
            "barcodeNumber" : "RSM1102", 
            "barcodePrice" : NumberInt(100), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Aroe alie Vera & neem daily face wash", 
            "barcodeNumber" : "RSM1103", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(1)
        }, 
        {
            "barcodeName" : "Aroe hibiscus and carrot daily face wash", 
            "barcodeNumber" : "RSM1104", 
            "barcodePrice" : NumberInt(75), 
            "barcodeStock" : NumberInt(1)
        }
    ]
#function calculates total Price from barcodePrice and gives missing barcodeStock as well 
totalPrice=0
for item in myarray:
    if len(item)==3:print("barcodeStock is missing /please check at "+str(item["barcodeNumber"]))
    totalPrice+=item.get("barcodePrice",0)
print("Number of barcodes/total bills in this kirana(+918008485850)=>"+str(len(myarray)))#example 573,559 , 919 , 465  ,1063  ,638

print("Total Bill from this kirana=>"+str(totalPrice))#example 69164.90000152588,50496,77240,65582.69999694824,125523.42999839783,90210

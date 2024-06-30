for rev in $(git log --format=%H); do
    git checkout $rev -- automation.py
    cp automation.py ../history/automation-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor1.py
    cp Extractor1.py ../history/Extractor1-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor101.py
    cp Extractor101.py ../history/Extractor101-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor102.py
    cp Extractor102.py ../history/Extractor102-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor103.py
    cp Extractor103.py ../history/Extractor103-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor104.py
    cp Extractor104.py ../history/Extractor104-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor105.py
    cp Extractor105.py ../history/Extractor105-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor106.py
    cp Extractor106.py ../history/Extractor106-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor107.py
    cp Extractor107.py ../history/Extractor107-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor108.py
    cp Extractor108.py ../history/Extractor108-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor109.py
    cp Extractor109.py ../history/Extractor109-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor110.py
    cp Extractor110.py ../history/Extractor110-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor360.py
    cp Extractor360.py ../history/Extractor360-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor3601.py
    cp Extractor3601.py ../history/Extractor3601-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor3603.py
    cp Extractor3603.py ../history/Extractor3603-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Extractor3604.py
    cp Extractor3604.py ../history/Extractor3604-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- ExtractorBarcodeI.py
    cp ExtractorBarcodeI.py ../history/ExtractorBarcodeI-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- ExtractorBarcodeI1.py
    cp ExtractorBarcodeI1.py ../history/ExtractorBarcodeI1-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- FaceBook.py
    cp FaceBook.py ../history/FaceBook-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- FaceBook2.py
    cp FaceBook2.py ../history/FaceBook2-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Keeper.py
    cp Keeper.py ../history/Keeper-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- kiranaViaPhoneNo.py
    cp kiranaViaPhoneNo.py ../history/kiranaViaPhoneNo-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- Naturalanguag.py
    cp Naturalanguag.py ../history/Naturalanguag-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- other1.py
    cp other1.py ../history/other1-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- other2.py
    cp other2.py ../history/other2-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- printer.py
    cp printer.py ../history/printer-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- RandomIdGenerator.py
    cp RandomIdGenerator.py ../history/RandomIdGenerator-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- SizeOfExtractor360.py
    cp SizeOfExtractor360.py ../history/SizeOfExtractor360-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- SizeOfExtractor3604TestCase.py
    cp SizeOfExtractor3604TestCase.py ../history/SizeOfExtractor3604TestCase-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- SizeOfExtractor3606.py
    cp SizeOfExtractor3606.py ../history/SizeOfExtractor3606-$rev.py
done

for rev in $(git log --format=%H); do
    git checkout $rev -- useApi.py
    cp useApi.py ../history/useApi-$rev.py
done
​

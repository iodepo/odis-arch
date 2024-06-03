from defs import regionFor

def main():
    print('regionsForFeature tests...')
    for feature in (
            'POLYGON ((-95.5 19.5,-95.5 31.5,-73.5 31.5,-73.5 19.5,-95.5 19.5))',
            'POLYGON ((144.401499 13.11742,144.401499 15.622688,145.8872 15.622688,145.8872 13.11742,144.401499 13.11742))',
            'POINT (0 0)',
            'POINT (-9 53)'
    ):
        print('    ', regionFor.feature(feature))

    print('regionForAddress tests...')
    for address in (
            'IOC Science and Communication Centre on Harmful Algae, University of Copenhagen - University of Copenhagen, Department of Biology - DK-1353 K\u00f8benhavn K - Denmark',
            'P. O. BOX LG 99 Legon-Accra, Ghana.',
    ):
        print('    ', regionFor.address(address))

    print('regionForName tests...')
    for name in (
            "Marine Science Country Profiles : Kenya",
            "The fisheries of Barbados and some of their problems",
            "Fiji : Where's the data?"
    ):
        print('    ', regionFor.name(name))

    print('regionForCountryOfLastProcessing tests...')
    for countryOfLastProcessing in (
            'Angola',
            'Panama',
            'Fiji'
    ):
        print('    ', regionFor.countryLastProcessing(countryOfLastProcessing))


if __name__ == '__main__':
    main()

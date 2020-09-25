SMK.INIT( {
    containerSel: '#smk-map-frame',
    config: [ './smk-config.json', '?smk-' ]
    // ?smk- added so that we do not have to update the catalogue code
} )
.then( function ( smk ) {
    // SMK initialized
} )

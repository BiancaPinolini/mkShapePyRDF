# cuts

cuts["supercut"] ={
    'expr': 'mll>50  \
            && ptll > 30 \
            && (Alt(Lepton_pdgId,0,0)*Alt(Lepton_pdgId,1,0)==-11*13 || \
                Alt(Lepton_pdgId,0,0)*Alt(Lepton_pdgId,1,0)==-11*11 || \
                Alt(Lepton_pdgId,0,0)*Alt(Lepton_pdgId,1,0)==-13*13)\
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>10 \
            && Alt(Lepton_pt,2,0.)<10 \
            && (MET_pt > 20 || PuppiMET_pt>20) \
            ',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}

# signal region

cuts["sr"] = {
    'expr': 'mjj>500 \
              && detajj > 3.5 \
              && Alt(CleanJet_pt,0,0.)>30 && Alt(CleanJet_pt,1,0.)>30 \
              && bVeto \
                 ' ,
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}

# cuts

cuts["supercut"] ={
    'expr': 'mll>50  \
            && ptll > 30 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && Alt(Lepton_pt,2,0.)<10 \
            && (MET_pt > 20 || PuppiMET_pt>20) \
            && Alt(Lepton_pdgId,0,0)*Alt(Lepton_pdgId,1,0)==-11*13 \
            && Alt(CleanJet_pt,0,0.)>30 && Alt(CleanJet_pt,1,0.)>30 \
            && mjj > 220 & detajj > 2 \
            ',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}

cuts["sr"] = {
   'expr': 'Zeppll_al < 1 && mth>60',# && bVeto',
   'parent' : 'supercut',
   'doVars': True,
   'doNumpy': True
}

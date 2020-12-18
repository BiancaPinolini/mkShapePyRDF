import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

###### START ######
# distance between lepton and jet
aliases['R_j1l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt(CleanJet_eta,0,-9999.)-Lepton_eta[0],2)+TMath::Power(Alt(CleanJet_phi,0,-9999.)-Lepton_phi[0],2))',
        'samples': mc + ['DATA']
}

aliases['R_j2l1'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt(CleanJet_eta,1,-9999.)-Lepton_eta[0],2)+TMath::Power(Alt(CleanJet_phi,1,-9999.)-Lepton_phi[0],2))',
        'samples': mc + ['DATA']
}

aliases['R_j1l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt(CleanJet_eta,0,-9999.)-Lepton_eta[1],2)+TMath::Power(Alt(CleanJet_phi,0,-9999.)-Lepton_phi[1],2))',
        'samples': mc + ['DATA']
}

aliases['R_j2l2'] = {
        'expr': 'TMath::Sqrt(TMath::Power(Alt(CleanJet_eta,1,-9999.)-Lepton_eta[1],2)+TMath::Power(Alt(CleanJet_phi,1,-9999.)-Lepton_phi[1],2))',
        'samples': mc + ['DATA']
}

# Zeppenfeld Variables
aliases['Zeppll_al'] = {
    'expr' : '0.5*fabs((Lepton_eta[0]+Lepton_eta[1])-(Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.)))'
}
aliases['Zepp1_al'] = {
    'expr' : 'Lepton_eta[0]-0.5*(Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))'
}
aliases['Zepp2_al'] = {
    'expr' : 'Lepton_eta[1]-0.5*(Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))'
}

# bVeto forward
# aliases['pT_forward']  = {
#     'expr'  : '(fabs(Alt(CleanJet_eta,0,-9999.)) > fabs(Alt(CleanJet_eta,1,-9999.))) * Alt(CleanJet_pt,0,-9999.) + (fabs(Alt(CleanJet_eta,1,-9999.)) >= fabs(Alt(CleanJet_eta,0,-9999.))) * Alt(CleanJet_pt,1,-9999.)',
#     'samples': mc + ['DATA']
# }
# aliases['eta_forward']  = {
#     'expr'  : '(fabs(Alt(CleanJet_eta,0,-9999.)) > fabs(Alt(CleanJet_eta,1,-9999.))) * abs(Alt(CleanJet_eta,0,-9999.)) + (fabs(Alt(CleanJet_eta,1,-9999.)) >= fabs(Alt(CleanJet_eta,0,-9999.))) * abs(Alt(CleanJet_eta,1,-9999.))',
#     'samples': mc + ['DATA']
# }
# aliases['btag_forward']  = {
#     'expr'  : '(fabs(Alt(CleanJet_eta,0,-9999.)) > fabs(Alt(CleanJet_eta,1,-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[0]] + (fabs(Alt(CleanJet_eta,1,-9999.)) >= fabs(Alt(CleanJet_eta,0,-9999.))) * Jet_btagDeepB[CleanJet_jetIdx[1]]',
#     'samples': mc + ['DATA']
# }
# aliases['bVetoForward'] = {
#     'expr': '(pT_forward>20. && eta_forward<2.5 && btag_forward>0.1241)==0',
#     'samples': mc + ['DATA']
# }

###### END ######

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

# Fake leptons transfer factor 
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)',
    'samples': mc
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum(AbsVec(GenPart_pdgId) == 6 && OddVec(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum((GenPart_pdgId == 6 && OddVec(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum((GenPart_pdgId == -6 && OddVec(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['Top_pTrw'] = {
    'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPtOTF) * TMath::Exp(0.0615 - 0.0005 * antitopGenPtOTF))) + isSingleTop',
    'samples': ['top']
}


# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# # No jet with pt > 30 GeV
# aliases['zeroJet'] = {
#     'expr': 'Alt(CleanJet_pt,0, 0) < 30.'
# }

# # ==1 jet with pt > 30 GeV
# aliases['oneJet'] = {
#     'expr': 'Alt(CleanJet_pt,0, 0) >= 30. && Alt(CleanJet_pt,1, 0) < 30.'
# }

# # ==2 jets with pt > 30 GeV
# aliases['twoJet'] = {
#     'expr': 'Alt(CleanJet_pt,0, 0) >= 30. && Alt(CleanJet_pt,1, 0) >= 30. && Alt(CleanJet_pt,2, 0) < 30.'
# }


aliases['zeroJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt(CleanJet_pt,0, 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt(CleanJet_pt,1, 0) > 30.'
}

# B tagging

aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4184) == 0' #0.4184
}

aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && AbsVec(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB,CleanJet_jetIdx) > 0.4184) >= 1' #0.4184
}

# CR definition

aliases['topcr'] = {
    'expr': '((zeroJet && !bVeto) || bReq)'
}

#########

# aliases['btag0'] = {
#     'expr': 'zeroJet && !bVeto'
# }

# aliases['btag1'] = {
#     'expr': 'oneJet && bReq'
# }

# aliases['btag2'] = {
#     'expr': 'twoJet && bReq'
# }

# aliases['bVetoSF'] = {
#     'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btag0SF'] = {
#     'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && CleanJet_pt<30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF,CleanJet_jetIdx)+1*(CleanJet_pt<20 || CleanJet_pt>30 || AbsVec(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btagnSF'] = {
#     'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF,CleanJet_jetIdx) + (CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))',
#     'samples': mc
# }

# aliases['btagSF'] = {
#     'expr': 'bVetoSF*bVeto + btag0SF*btag0 + btagnSF*(btag1 + btag2) + (!bVeto && !btag0 && !btag1 && !btag2)',
#     'samples': mc
# }

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF,CleanJet_jetIdx)+1*(CleanJet_pt<20 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}


aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && AbsVec(CleanJet_eta)<2.5)*Take(Jet_btagSF,CleanJet_jetIdx)+1*(CleanJet_pt<30 || AbsVec(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'samples': mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']), # removed PUJetSF (not in trees)
    'samples': mc
}

# # remove SFweight2l (0-weight events)
# aliases['SFweight'] = {
#     'expr': ' * '.join(['LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']), # removed PUJetSF (not in trees)
#     'samples': mc
# }


# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}


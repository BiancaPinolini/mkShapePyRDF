# variables

#variables = {}

#
variables['Mll']  = {       'name': 'mll',            #   variable name
                            'range' : (20,0,200),   #   variable range
                            'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                        }


variables['ptll']    = {    'name': 'ptll',            #   variable name
                            'range' : (20,0,200),   #   variable range
                            'xaxis' : 'pt_{ll} [GeV]',  #   x axis name
                        }
variables['Mjj']  = {       'name': 'mjj',            #   variable name
                            'range' : (15,0,3000),   #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                        }

variables['mth']  = {   'name': 'mth',            #   variable name
                        'range' : (20,0,400),    #   variable range
                        'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                        }
variables['mTi']  = {   'name': 'mTi',            #   variable name
                        'range' : (20,0,400),    #   variable range
                        'xaxis' : 'm_{Ti} [GeV]',  #   x axis name
                        }
variables['detajj']  = {   'name': 'abs(detajj)',
                            'range' : (20,0,9),
                        '    xaxis' : '#Delta#eta_{jj}',

                        }
variables['pt1']  = {   'name': 'Alt(Lepton_pt,0,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 1st lep'
                        }


variables['pt2']  = {   'name': 'Alt(Lepton_pt,1,-9999.)',
                        'range' : (20,0.,200),
                        'xaxis' : 'p_{T} 2nd lep'
                        }
variables['eta1']  = {   'name': 'Alt(Lepton_eta,0,-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 1st lep'
                        }


variables['eta2']  = {   'name': 'Alt(Lepton_eta,1,-9999.)',
                        'range' : (40,-3.14,3.14),
                        'xaxis' : 'p_{T} 2nd lep'
                        }


variables['jeteta1'] = {  'name': 'Alt(CleanJet_eta,0,-9999.)',
                        'range': (10,-5,5),
                        'xaxis': 'eta_{j1}',
                        }

variables['jeteta2'] = {         'name': 'Alt(CleanJet_eta,1,-9999.)',
                               'range': (20,-5,5),
                               'xaxis': 'eta_{j2}',

                               }


variables['Zlep1']  = {  'name': '(Alt(Lepton_eta,0,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj',
                         'range': (200,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{1}',
                         }

variables['Zlep2']  = {  'name': '(Alt(Lepton_eta,1,-9999.) - (Alt(CleanJet_eta,0,-9999.)+Alt(CleanJet_eta,1,-9999.))/2)/detajj',
                         'range': (200,-1.5,1.5),
                         'xaxis': 'Z^{lep}_{2}',
                         }
variables['jetpt1']  = {   'name': 'Alt(CleanJet_pt,0,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 1st jet'
                           }

variables['jetpt2']  = {   'name': 'Alt(CleanJet_pt,1,-9999.)',
                           'range' : (15,0.,300),
                           'xaxis' : 'p_{T} 2nd jet'
                           }

variables['met']  = {   'name': 'MET_pt',            #   variable name
                        'range' : (50,0,250),    #   variable range
                        'xaxis' : 'MET [GeV]',  #   x axis name
                        }
variables['nJet']  = {   'name': 'Sum(CleanJet_pt>30)',
                         'range' : (4,0,4),
                         'xaxis' : 'njets'
                         }

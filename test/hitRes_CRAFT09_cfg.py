import FWCore.ParameterSet.Config as cms

process = cms.Process("ReRec")

process.load("CondCore.CondDB.CondDB_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
# pointing skim
'/store/data/Run2018C/Cosmics/ALCARECO/TkAlCosmics0T-PromptReco-v1/000/319/353/00000/C48116EA-EA84-E811-A43C-FA163E1461B4.root'
    )
)

# output module#
#process.load("Configuration.EventContent.EventContentCosmics_cff")
#process.load("CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi")
#process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
#process.load("RecoTracker.MeasurementDet.MeasurementTrackerESProducer_cfi")

# Conditions (Global Tag is used here):
process.load("Configuration.Geometry.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '101X_dataRun2_Prompt_v11'
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

#Geometry
#process.load("Configuration.StandardSequences.Geometry_cff")

# Real data raw to digi
#process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

# reconstruction sequence for Cosmics
#process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

# offline DQM
#process.load("DQMOffline.Configuration.DQMOfflineCosmics_cff")
#process.load("DQMServices.Components.MEtoEDMConverter_cff")

#L1 trigger validation
#process.load("L1Trigger.HardwareValidation.L1HardwareValidation_cff")
#process.load("L1Trigger.Configuration.L1Config_cff")
#process.load("L1TriggerConfig.CSCTFConfigProducers.CSCTFConfigProducer_cfi")
#process.load("L1TriggerConfig.CSCTFConfigProducers.L1MuCSCTFConfigurationRcdSrc_cfi")

#process.load("RecoTracker.TrackProducer.TrackRefitters_cff")


process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("Configuration.Geometry.GeometryDB_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process, 'ALCARECOTkAlCosmicsCTF0T',
                                                     isPVValidation=False,
                                                     TTRHBuilder='WithAngleAndTemplate',
                                                     usePixelQualityFlag=True,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=True,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=True,
                                                     use_d0cut=False,
                                                    )
process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")


import Alignment.CommonAlignment.tools.trackselectionRefitting as trackselRefit
process.seqTrackselRefit = trackselRefit.getSequence(process, 'ALCARECOTkAlCosmicsCTF0T',
                                                     isPVValidation=False,
                                                     TTRHBuilder='WithAngleAndTemplate',
                                                     usePixelQualityFlag=True,
                                                     openMassWindow=False,
                                                     cosmicsDecoMode=True,
                                                     cosmicsZeroTesla=False,
                                                     momentumConstraint=None,
                                                     cosmicTrackSplitting=False,
                                                     use_d0cut=False,
                                                    )


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('HitRes.root')
)

process.analysis = cms.EDFilter("HitRes",
    usePXB = cms.bool(True),
    usePXF = cms.bool(True),
    useTIB = cms.bool(True),
    useTOB = cms.bool(True),
    useTID = cms.bool(True),
    useTEC = cms.bool(True),
    ROUList = cms.vstring('TrackerHitsTIBLowTof', 
        'TrackerHitsTIBHighTof', 
        'TrackerHitsTOBLowTof', 
        'TrackerHitsTOBHighTof'),
    trajectories = cms.InputTag("FinalTrackRefitter"),
    associatePixel = cms.bool(False),
    associateStrip = cms.bool(False),
    associateRecoTracks = cms.bool(False),
    tracks = cms.InputTag("FinalTrackRefitter"),
    barrelOnly = cms.bool(False)
)

# Path and EndPath definitions
process.p = cms.Path(process.seqTrackselRefit*process.analysis)
#process.endjob_step = cms.Path(process.endOfProcess)

# Schedule definition
#process.schedule = cms.Schedule(process.p,process.endjob_step)
process.schedule = cms.Schedule(process.p)

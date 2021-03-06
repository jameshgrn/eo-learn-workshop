# load sample eopatch
eopatch = EOPatch.load('../data/sentinel1_sample', lazy_loading=True)

# create task using data from sample eopatch
reactiv = ReactivTask((FeatureType.DATA_TIMELESS, 'speckle_variability'),
                      data_feature=(FeatureType.DATA, 'IW_VV'),
                      mask_feature=(FeatureType.MASK, 'IS_DATA'))

# run the task
eopatch = reactiv.execute(eopatch)

# plot the results
plot_results(eopatch[(FeatureType.DATA_TIMELESS, 'speckle_variability')])
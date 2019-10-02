def unify_dataframes_axis(dataframes, axis):

    if axis == 0:

        elements = dataframes[0].index

    else:

        elements = dataframes[0].columns

    for dataframe in dataframes[1:]:

        if axis == 0:

            elements &= dataframe.index

        else:

            elements &= dataframe.columns

    elements = elements.sort_values()

    assert 0 < elements.size

    if axis == 0:

        dataframes = tuple(dataframe.loc[elements] for dataframe in dataframes)

    else:

        dataframes = tuple(dataframe[elements] for dataframe in dataframes)

    return dataframes

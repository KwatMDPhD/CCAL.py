from numpy import absolute


def get_signal_to_noise(ve0, ve1):

    me0 = ve0.mean()

    me1 = ve1.mean()

    st0 = ve0.std()

    st1 = ve1.std()

    lo0 = 0.2 * absolute(me0)

    lo1 = 0.2 * absolute(me1)

    if me0 == 0:

        me0 = 1

        st0 = 0.2

    elif st0 < lo0:

        st0 = lo0

    if me1 == 0:

        me1 = 1

        st1 = 0.2

    elif st1 < lo1:

        st1 = lo1

    return (me1 - me0) / (st0 + st1)

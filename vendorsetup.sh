# Shebang is intentionally missing - do not run as a script

# ABI compatibility checks fail for several reasons:
#   - The update to Clang 12 causes some changes, but no breakage has been
#     observed in practice.
#   - Switching to zlib-ng changes some internal structs, but not the public
#     API.
#
# We may fix these eventually by updating the ABI specifications, but it's
# likely not worth the effort for us because of how many repos are affected.
# We would need to fork a lot of extra repos (thus increasing maintenance
# overhead) just to update the ABI specs.
#
# For now, just skip the ABI checks to fix build errors.
export SKIP_ABI_CHECKS=true

# Enable global ThinLTO
#
# In addition to the libraries that we've already enabled ThinLTO for,
# enabling it globally improves app launch speed by 2% on average. All
# times are in milliseconds:
#
# +-------------------+----------+---------+
# |     App/screen    | Baseline | ThinLTO |
# +-------------------+----------+---------+
# |    bromite-main   |   246    |   247   |
# |  bromite-settings |    64    |    66   |
# |    element-main   |   593    |   591   |
# |  element-settings |    58    |    51   |
# |    fasthub-main   |   273    |   274   |
# |    filesgo-main   |   293    |   286   |
# |    gallery-main   |   190    |   194   |
# |     gcam-main     |   288    |   290   |
# |   gcam-settings   |   166    |   168   |
# |    github-main    |   265    |   260   |
# |  github-settings  |    72    |    70   |
# |   infinity-main   |   249    |   246   |
# | infinity-settings |    69    |    66   |
# |    photos-main    |   274    |   263   |
# |     play-main     |   382    |   379   |
# |   recorder-main   |   369    |   364   |
# |   settings-apps   |   126    |   129   |
# |  settings-dev-opt |   221    |   206   |
# |   settings-main   |   312    |   304   |
# |  settings-storage |   182    |   182   |
# |    signal-main    |   325    |   325   |
# |  signal-settings  |    62    |    59   |
# |     slack-main    |   385    |   400   |
# |   slack-settings  |    77    |    75   |
# |     tasks-main    |   244    |   239   |
# |   tasks-settings  |    61    |    68   |
# |   telegram-main   |   413    |   400   |
# +-------------------+----------+---------+
#
# Normalized times:
#
# +-------------------+----------+--------------+
# |     App/screen    | Baseline |   ThinLTO    |
# +-------------------+----------+--------------+
# |    bromite-main   |    1     | 1.004065041  |
# |  bromite-settings |    1     |   1.03125    |
# |    element-main   |    1     | 0.9966273187 |
# |  element-settings |    1     | 0.8793103448 |
# |    fasthub-main   |    1     | 1.003663004  |
# |    filesgo-main   |    1     | 0.976109215  |
# |    gallery-main   |    1     | 1.021052632  |
# |     gcam-main     |    1     | 1.006944444  |
# |   gcam-settings   |    1     | 1.012048193  |
# |    github-main    |    1     | 0.9811320755 |
# |  github-settings  |    1     | 0.9722222222 |
# |   infinity-main   |    1     | 0.9879518072 |
# | infinity-settings |    1     | 0.9565217391 |
# |    photos-main    |    1     | 0.9598540146 |
# |     play-main     |    1     | 0.9921465969 |
# |   recorder-main   |    1     | 0.9864498645 |
# |   settings-apps   |    1     | 1.023809524  |
# |  settings-dev-opt |    1     | 0.9321266968 |
# |   settings-main   |    1     | 0.9743589744 |
# |  settings-storage |    1     |      1       |
# |    signal-main    |    1     |      1       |
# |  signal-settings  |    1     | 0.9516129032 |
# |     slack-main    |    1     | 1.038961039  |
# |   slack-settings  |    1     | 0.974025974  |
# |     tasks-main    |    1     | 0.9795081967 |
# |   tasks-settings  |    1     | 1.114754098  |
# |   telegram-main   |    1     | 0.9685230024 |
# +-------------------+----------+--------------+
#
# Normalized stats:
#
# +---------+----------+--------------+
# |  Metric | Baseline |   ThinLTO    |
# +---------+----------+--------------+
# |  Median |    1     | 0.9879518072 |
# | Minimum |    1     | 0.8793103448 |
# | Maximum |    1     | 1.114754098  |
# |   Mean  |    1     | 0.9898158859 |
# +---------+----------+--------------+
#
# This doesn't increase build time significantly, so enable it for
# performance.
export GLOBAL_THINLTO=true

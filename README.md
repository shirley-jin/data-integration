# data-integration
A tool to combine all the values with the same ID under the same category

an example:

original data:

|user_id|topic|gamma|
|-------|-----|-----|
|276836|1|0.3387|
|276836|20|0.3700|
|428066|20|0.7018|
|428066|20|0.3173|
|430444|20|0.5197|
|845107|1|0.3861|
|845107|12|0.4461|
|30014533|1|0.9388|
|30014533|1|0.3046|
|50174802|1|0.4499|
|50174802|1|0.4049|

Integrated data

|user_id|topic|gamma|
|-------|-----|-----|
|276836|1|0.3387|
|276836|20|0.3700|
|428066|20|1.0191|
|430444|20|0.5197|
|845107|1|0.3861|
|845107|12|0.4461|
|30014533|1|1.2434|
|50174802|1|0.8548|

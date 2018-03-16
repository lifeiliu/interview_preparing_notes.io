# connect to INTERNET

## 1. get the permission
in the manifests -> AndroidManifest.xml
```
<uses-permission android:name="android.permission.INTERNET"/>
```
## 2. build the URL using uri and query parameters
```
Uri buildUri = Uri.parse(BASE_URL).buildUpon
				.appendQueryParameter(Parameter1, value1)
				.appendQueryParameter(Parameter5, value5)
				.bulid();
URL url = new URL(bulitUri.toString());
```

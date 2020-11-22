testOutput = """
------------------------------------------------------------
Project :trendyol_v2
------------------------------------------------------------

prodRuntimeClasspath - Runtime classpath of compilation 'prod' (target  (androidJvm)).
+--- androidx.databinding:databinding-common:4.0.1
+--- androidx.databinding:databinding-runtime:4.0.1
|    +--- androidx.lifecycle:lifecycle-runtime:2.0.0 -> 2.2.0
|    |    +--- androidx.lifecycle:lifecycle-common:2.2.0
|    |    |    \--- androidx.annotation:annotation:1.1.0
|    |    +--- androidx.arch.core:core-common:2.1.0
|    |    |    \--- androidx.annotation:annotation:1.1.0
|    |    \--- androidx.annotation:annotation:1.1.0
|    +--- androidx.collection:collection:1.0.0 -> 1.1.0
|    |    \--- androidx.annotation:annotation:1.1.0
|    \--- androidx.databinding:databinding-common:4.0.1
+--- androidx.databinding:databinding-adapters:4.0.1
|    +--- androidx.databinding:databinding-common:4.0.1
|    \--- androidx.databinding:databinding-runtime:4.0.1 (*)
+--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0
|    \--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0
|         +--- org.jetbrains.kotlin:kotlin-stdlib-common:1.4.0
|         \--- org.jetbrains:annotations:13.0
+--- project :osiris
|    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
+--- project :scalinglib
|    +--- androidx.coordinatorlayout:coordinatorlayout:1.1.0
|    |    +--- androidx.annotation:annotation:1.1.0
|    |    +--- androidx.core:core:1.1.0 -> 1.2.0
|    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    +--- androidx.lifecycle:lifecycle-runtime:2.0.0 -> 2.2.0 (*)
|    |    |    +--- androidx.versionedparcelable:versionedparcelable:1.1.0
|    |    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    +--- androidx.customview:customview:1.0.0
|    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    \--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    \--- com.google.android.material:material:1.1.0
|         +--- androidx.annotation:annotation:1.0.1 -> 1.1.0
|         +--- androidx.appcompat:appcompat:1.1.0
|         |    +--- androidx.annotation:annotation:1.1.0
|         |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         |    +--- androidx.cursoradapter:cursoradapter:1.0.0
|         |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1
|         |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         |    |    +--- androidx.collection:collection:1.1.0 (*)
|         |    |    +--- androidx.viewpager:viewpager:1.0.0
|         |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|         |    |    |    \--- androidx.customview:customview:1.0.0 (*)
|         |    |    +--- androidx.loader:loader:1.0.0
|         |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|         |    |    |    +--- androidx.lifecycle:lifecycle-livedata:2.0.0 -> 2.2.0
|         |    |    |    |    +--- androidx.arch.core:core-runtime:2.1.0
|         |    |    |    |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    |    |    |    \--- androidx.arch.core:core-common:2.1.0 (*)
|         |    |    |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.2.0
|         |    |    |    |    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|         |    |    |    |    |    +--- androidx.arch.core:core-common:2.1.0 (*)
|         |    |    |    |    |    \--- androidx.arch.core:core-runtime:2.1.0 (*)
|         |    |    |    |    \--- androidx.arch.core:core-common:2.1.0 (*)
|         |    |    |    \--- androidx.lifecycle:lifecycle-viewmodel:2.0.0 -> 2.2.0
|         |    |    |         \--- androidx.annotation:annotation:1.1.0
|         |    |    +--- androidx.activity:activity:1.1.0
|         |    |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         |    |    |    +--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|         |    |    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|         |    |    |    +--- androidx.savedstate:savedstate:1.0.0
|         |    |    |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    |    |    +--- androidx.arch.core:core-common:2.0.1 -> 2.1.0 (*)
|         |    |    |    |    \--- androidx.lifecycle:lifecycle-common:2.0.0 -> 2.2.0 (*)
|         |    |    |    \--- androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0 -> 2.2.0
|         |    |    |         +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    |    |         +--- androidx.savedstate:savedstate:1.0.0 (*)
|         |    |    |         +--- androidx.lifecycle:lifecycle-livedata-core:2.2.0 (*)
|         |    |    |         \--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|         |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.2.0 (*)
|         |    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|         |    |    \--- androidx.lifecycle:lifecycle-viewmodel-savedstate:2.2.0 (*)
|         |    +--- androidx.appcompat:appcompat-resources:1.1.0
|         |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    +--- androidx.core:core:1.0.1 -> 1.2.0 (*)
|         |    |    +--- androidx.vectordrawable:vectordrawable:1.1.0
|         |    |    |    +--- androidx.annotation:annotation:1.1.0
|         |    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         |    |    |    \--- androidx.collection:collection:1.1.0 (*)
|         |    |    +--- androidx.vectordrawable:vectordrawable-animated:1.1.0
|         |    |    |    +--- androidx.vectordrawable:vectordrawable:1.1.0 (*)
|         |    |    |    +--- androidx.interpolator:interpolator:1.0.0
|         |    |    |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    |    |    \--- androidx.collection:collection:1.1.0 (*)
|         |    |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|         |    +--- androidx.drawerlayout:drawerlayout:1.0.0
|         |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|         |    |    \--- androidx.customview:customview:1.0.0 (*)
|         |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|         +--- androidx.cardview:cardview:1.0.0
|         |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         +--- androidx.coordinatorlayout:coordinatorlayout:1.1.0 (*)
|         +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|         +--- androidx.lifecycle:lifecycle-runtime:2.0.0 -> 2.2.0 (*)
|         +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0
|         |    +--- androidx.annotation:annotation:1.1.0
|         |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|         |    +--- androidx.customview:customview:1.0.0 (*)
|         |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|         +--- androidx.transition:transition:1.2.0
|         |    +--- androidx.annotation:annotation:1.1.0
|         |    +--- androidx.core:core:1.0.1 -> 1.2.0 (*)
|         |    \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|         +--- androidx.vectordrawable:vectordrawable:1.1.0 (*)
|         \--- androidx.viewpager2:viewpager2:1.0.0
|              +--- androidx.annotation:annotation:1.1.0
|              +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|              +--- androidx.recyclerview:recyclerview:1.1.0 (*)
|              +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|              \--- androidx.collection:collection:1.1.0 (*)
+--- project :libraries:remote
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.squareup.retrofit2:retrofit:2.5.0
|    |    \--- com.squareup.okhttp3:okhttp:3.12.0 -> 3.12.10
|    |         \--- com.squareup.okio:okio:1.15.0 -> 2.2.2
|    |              \--- org.jetbrains.kotlin:kotlin-stdlib:1.2.60 -> 1.4.0 (*)
|    +--- com.squareup.okhttp3:logging-interceptor:3.12.2
|    |    \--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    +--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    +--- com.trendyol.android-core:resource:1.0.3
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.4.0
|    |    |         \--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    \--- io.reactivex.rxjava2:rxjava:2.2.17
|    |         \--- org.reactivestreams:reactive-streams:1.0.3
|    +--- com.trendyol.android-core:status:1.0.0
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    \--- com.github.Trendyol:StateLayout:1.4.3 -> 1.4.4
|    |         +--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.41 -> 1.4.0 (*)
|    |         \--- androidx.appcompat:appcompat:1.0.2 -> 1.1.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27
|    |    \--- javax.inject:javax.inject:1
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- com.squareup.retrofit2:converter-gson:2.5.0
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    \--- com.google.code.gson:gson:2.8.2 -> 2.8.6
|    +--- com.squareup.retrofit2:adapter-rxjava2:2.5.0
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    \--- io.reactivex.rxjava2:rxjava:2.0.0 -> 2.2.17 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1
|    |    \--- io.reactivex.rxjava2:rxjava:2.2.6 -> 2.2.17 (*)
|    +--- com.facebook.stetho:stetho-okhttp3:1.5.1
|    |    +--- com.facebook.stetho:stetho:1.5.1
|    |    |    +--- commons-cli:commons-cli:1.2
|    |    |    +--- com.google.code.findbugs:jsr305:2.0.1
|    |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    +--- com.google.code.findbugs:jsr305:2.0.1
|    |    \--- com.squareup.okhttp3:okhttp:3.4.2 -> 3.12.10 (*)
|    +--- com.trendyol.android-core:reporter:1.1.0
|    |    +--- androidx.databinding:databinding-common:3.6.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.6.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    \--- com.google.firebase:firebase-crashlytics:17.1.0
|    |         +--- com.google.android.datatransport:transport-api:2.2.0
|    |         +--- com.google.android.datatransport:transport-backend-cct:2.2.3
|    |         |    +--- androidx.annotation:annotation:1.1.0
|    |         |    +--- com.google.android.datatransport:transport-api:2.2.0
|    |         |    +--- com.google.android.datatransport:transport-runtime:2.2.3
|    |         |    |    +--- androidx.annotation:annotation:1.1.0
|    |         |    |    +--- com.google.android.datatransport:transport-api:2.2.0
|    |         |    |    \--- com.google.dagger:dagger:2.27 (*)
|    |         |    \--- com.google.firebase:firebase-encoders-json:16.1.0
|    |         |         \--- androidx.annotation:annotation:1.1.0
|    |         +--- com.google.android.datatransport:transport-runtime:2.2.3 (*)
|    |         +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2
|    |         |    \--- com.google.android.gms:play-services-basement:17.2.1
|    |         |         +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |         |         +--- androidx.core:core:1.2.0 (*)
|    |         |         \--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |         +--- com.google.firebase:firebase-common:19.3.0
|    |         |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |         |    +--- com.google.auto.value:auto-value-annotations:1.6.5
|    |         |    \--- com.google.firebase:firebase-components:16.0.0
|    |         |         \--- androidx.annotation:annotation:1.1.0
|    |         +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |         +--- com.google.firebase:firebase-encoders-json:16.1.0 (*)
|    |         +--- com.google.firebase:firebase-iid:20.1.5 -> 20.2.3
|    |         |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |         |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |         |    +--- androidx.legacy:legacy-support-core-utils:1.0.0
|    |         |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |         |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |         |    |    +--- androidx.documentfile:documentfile:1.0.0
|    |         |    |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |         |    |    +--- androidx.loader:loader:1.0.0 (*)
|    |         |    |    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0
|    |         |    |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |         |    |    \--- androidx.print:print:1.0.0
|    |         |    |         \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |         |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         |    +--- com.google.android.gms:play-services-stats:17.0.0
|    |         |    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |         |    |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |         |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |         |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |         |    +--- com.google.firebase:firebase-iid-interop:17.0.0
|    |         |    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0
|    |         |    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |         |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |         |    |    |    +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |         |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         |    |    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |         |    |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         |    +--- com.google.firebase:firebase-installations:16.3.2
|    |         |    |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |         |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |         |    |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |         |    |    \--- com.google.firebase:firebase-installations-interop:16.0.0
|    |         |    |         \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |         |    \--- com.google.firebase:firebase-installations-interop:16.0.0 (*)
|    |         +--- com.google.firebase:firebase-iid-interop:17.0.0 (*)
|    |         +--- com.google.firebase:firebase-measurement-connector:18.0.0
|    |         |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |         \--- com.squareup.okhttp3:okhttp:3.12.1 -> 3.12.10 (*)
|    +--- project :features:legacy
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    +--- project :features:model
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    \--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    \--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- project :features:advertisingid
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    \--- com.google.android.gms:play-services-ads-identifier:17.0.0
|    |         \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    +--- project :features:common
|    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    +--- project :libraries:extensions
|    |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    |    |    +--- androidx.constraintlayout:constraintlayout:1.1.3
|    |    |    |    \--- androidx.constraintlayout:constraintlayout-solver:1.1.3
|    |    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    |    +--- project :dolap-lite:ui-components
|    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    |    +--- javax.inject:javax.inject:1
|    |    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    |    |    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    |    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    |    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    |    |    +--- androidx.drawerlayout:drawerlayout:1.0.0 (*)
|    |    |    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    |    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    |    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    |    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    |    |    +--- com.trendyol.android-core:android-extensions:1.0.7
|    |    |    |    |    +--- androidx.databinding:databinding-common:3.6.0 -> 4.0.1
|    |    |    |    |    +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|    |    |    |    |    +--- androidx.databinding:databinding-adapters:3.6.0 -> 4.0.1 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    |    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    |    |    +--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
|    |    |    |    |    \--- androidx.core:core-ktx:1.0.1 -> 1.1.0
|    |    |    |    |         +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.31 -> 1.4.0 (*)
|    |    |    |    |         +--- androidx.annotation:annotation:1.1.0
|    |    |    |    |         \--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    |    |    |    +--- com.trendyol.android-core:generic-extensions:1.0.5
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.4.0 (*)
|    |    |    |    |    \--- io.reactivex.rxjava2:rxjava:2.2.17 (*)
|    |    |    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    |    |    +--- com.trendyol.android-core:view-extensions:1.0.0
|    |    |    |    |    +--- androidx.databinding:databinding-common:3.6.0 -> 4.0.1
|    |    |    |    |    +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|    |    |    |    |    +--- androidx.databinding:databinding-adapters:3.6.0 -> 4.0.1 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    |    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    |    |    +--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
|    |    |    |    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    |    |    |    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0
|    |    |    |    |    |    +--- com.github.bumptech.glide:gifdecoder:4.11.0
|    |    |    |    |    |    |    \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    |    +--- com.github.bumptech.glide:disklrucache:4.11.0
|    |    |    |    |    |    +--- com.github.bumptech.glide:annotations:4.11.0
|    |    |    |    |    |    +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |    |    |    |    |    +--- androidx.vectordrawable:vectordrawable-animated:1.0.0 -> 1.1.0 (*)
|    |    |    |    |    |    \--- androidx.exifinterface:exifinterface:1.0.0
|    |    |    |    |    |         \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    \--- com.trendyol.android-core:generic-extensions:1.0.2 -> 1.0.5 (*)
|    |    |    |    \--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    |    |    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    |    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    |    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    |    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    |    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    |    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    |    \--- com.jakewharton.rxbinding2:rxbinding:2.2.0
|    |    |         +--- io.reactivex.rxjava2:rxjava:2.2.2 -> 2.2.17 (*)
|    |    |         +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    |         \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    +--- project :features:model (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    |    +--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-extensions:2.2.0
|    |    |    +--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|    |    |    +--- androidx.arch.core:core-common:2.1.0 (*)
|    |    |    +--- androidx.arch.core:core-runtime:2.1.0 (*)
|    |    |    +--- androidx.fragment:fragment:1.2.0 -> 1.2.1 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-livedata:2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-process:2.2.0
|    |    |    |    \--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-service:2.2.0
|    |    |    |    \--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|    |    |    \--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    +--- com.jakewharton.rxbinding2:rxbinding:2.2.0 (*)
|    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    \--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    \--- com.github.chuckerteam.chucker:library:3.2.0
|         +--- androidx.databinding:viewbinding:3.6.1 -> 4.0.1 (*)
|         +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.71 -> 1.4.0 (*)
|         +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.71 -> 1.4.0 (*)
|         +--- com.google.android.material:material:1.1.0 (*)
|         +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|         +--- androidx.lifecycle:lifecycle-viewmodel-ktx:2.2.0
|         |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.50 -> 1.4.0 (*)
|         |    +--- org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.0 -> 1.3.5
|         |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.70 -> 1.4.0 (*)
|         |    |    \--- org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.5
|         |    |         +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.70 -> 1.4.0 (*)
|         |    |         \--- org.jetbrains.kotlin:kotlin-stdlib-common:1.3.70 -> 1.4.0
|         |    \--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|         +--- androidx.lifecycle:lifecycle-livedata-ktx:2.2.0
|         |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.50 -> 1.4.0 (*)
|         |    +--- org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.0 -> 1.3.5 (*)
|         |    +--- androidx.lifecycle:lifecycle-livedata:2.2.0 (*)
|         |    \--- androidx.lifecycle:lifecycle-livedata-core-ktx:2.2.0
|         |         +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.50 -> 1.4.0 (*)
|         |         \--- androidx.lifecycle:lifecycle-livedata-core:2.2.0 (*)
|         +--- androidx.room:room-ktx:2.2.5
|         |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.41 -> 1.4.0 (*)
|         |    +--- org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.0 -> 1.3.5 (*)
|         |    +--- androidx.room:room-common:2.2.5
|         |    |    \--- androidx.annotation:annotation:1.1.0
|         |    \--- androidx.room:room-runtime:2.2.5
|         |         +--- androidx.room:room-common:2.2.5 (*)
|         |         +--- androidx.sqlite:sqlite-framework:2.0.1 -> 2.1.0
|         |         |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |         |    \--- androidx.sqlite:sqlite:2.1.0
|         |         |         \--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |         +--- androidx.sqlite:sqlite:2.0.1 -> 2.1.0 (*)
|         |         \--- androidx.arch.core:core-runtime:2.0.1 -> 2.1.0 (*)
|         +--- androidx.room:room-runtime:2.2.5 (*)
|         +--- org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.5 (*)
|         +--- org.jetbrains.kotlinx:kotlinx-coroutines-android:1.3.5 (*)
|         +--- com.google.code.gson:gson:2.8.6
|         \--- com.squareup.okhttp3:okhttp:3.12.10 (*)
+--- project :libraries:local
|    +--- project :features:legacy (*)
|    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- androidx.room:room-rxjava2:2.2.3
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.9 -> 2.2.17 (*)
|    |    +--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
|    |    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    \--- androidx.arch.core:core-runtime:2.0.1 -> 2.1.0 (*)
|    +--- androidx.sqlite:sqlite:2.1.0 (*)
|    +--- androidx.sqlite:sqlite-framework:2.1.0 (*)
|    \--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
+--- project :features:common (*)
+--- project :features:cart-operations
|    +--- project :features:model (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- javax.inject:javax.inject:1
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:legacy (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    \--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
+--- project :features:configuration
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:common (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
|    \--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- project :features:location-search
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.android.gms:play-services-maps:17.0.0
|    |    +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- project :libraries:remote (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
+--- project :features:user-operations
|    +--- project :features:configuration (*)
|    +--- project :features:legacy (*)
|    +--- project :libraries:local (*)
|    +--- project :libraries:remote (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- project :features:common (*)
|    +--- androidx.lifecycle:lifecycle-process:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    +--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.trendyol.android-core:reporter:1.1.0 (*)
|    \--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
+--- project :libraries:extensions (*)
+--- project :features:model (*)
+--- project :features:legacy (*)
+--- project :features:advertisingid (*)
+--- project :libraries:deeplink-dispatcher
|    +--- project :features:user-operations (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- com.github.Trendyol:medusa:0.9.1-rc
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.50 -> 1.4.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- project :libraries:extensions (*)
|    +--- project :libraries:remote (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    \--- javax.inject:javax.inject:1
+--- project :features:ab-test
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- project :features:legacy (*)
|    \--- javax.inject:javax.inject:1
+--- project :libraries:widgets
|    +--- project :features:model (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:legacy (*)
|    +--- project :features:configuration (*)
|    +--- com.trendyol.android-core:status:1.0.0 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- project :features:common (*)
|    +--- project :libraries:extensions (*)
|    +--- project :libraries:vertical-product-card-view
|    |    +--- project :features:model (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    \--- project :features:legacy (*)
|    +--- project :libraries:boutique-count-down-view
|    |    +--- project :features:model (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    +--- project :libraries:extensions (*)
|    |    +--- project :features:common (*)
|    |    +--- project :features:legacy (*)
|    |    \--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :osiris (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.facebook.shimmer:shimmer:0.5.0
|    |    \--- androidx.annotation:annotation:1.0.1 -> 1.1.0
|    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    +--- com.github.MertNYuksel:CircleIndicator:2a2e973374
|    |    +--- com.github.MertNYuksel.CircleIndicator:circleindicator:2a2e973374
|    |    |    \--- androidx.annotation:annotation:1.1.0
|    |    \--- com.github.MertNYuksel.CircleIndicator:LoopingViewPager:2a2e973374
|    |         +--- androidx.viewpager:viewpager:1.0.0 (*)
|    |         \--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    +--- com.github.erkutaras:impression:0.0.3
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.41 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.0.2 -> 1.1.0 (*)
|    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.0.2 -> 1.1.0 (*)
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.41 -> 1.4.0 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    \--- com.trendyol.android-core:base:1.0.4
|         +--- androidx.databinding:databinding-common:3.6.0 -> 4.0.1
|         +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|         +--- androidx.databinding:databinding-adapters:3.6.0 -> 4.0.1 (*)
|         +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|         +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|         +--- androidx.appcompat:appcompat:1.1.0 (*)
|         +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|         +--- com.google.dagger:dagger-android:2.26
|         |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|         |    +--- androidx.annotation:annotation:1.1.0
|         |    \--- javax.inject:javax.inject:1
|         +--- com.google.dagger:dagger-android-support:2.26
|         |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|         |    +--- com.google.dagger:dagger-android:2.26 (*)
|         |    +--- androidx.annotation:annotation:1.1.0
|         |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|         |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|         |    \--- javax.inject:javax.inject:1
|         +--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
|         \--- androidx.recyclerview:recyclerview:1.1.0 (*)
+--- project :features:seller-store
|    +--- project :features:user-operations (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- project :libraries:remote (*)
|    +--- project :libraries:extensions (*)
|    +--- project :libraries:widgets (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1
|    |    +--- androidx.databinding:databinding-common:3.6.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.6.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    \--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
|    \--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
+--- project :libraries:vertical-product-card-view (*)
+--- project :features:in-app-popup
|    +--- project :features:user-operations (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :libraries:extensions (*)
|    +--- project :libraries:local (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:legacy (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.trendyol.android-core:reporter:1.1.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    \--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
+--- project :features:address:operations
|    +--- project :libraries:local (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- javax.inject:javax.inject:1
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :libraries:remote (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    \--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
+--- project :features:checkout
|    +--- project :dolap-lite:ui-components (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- project :libraries:extensions (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    \--- com.trendyol.android-core:view-extensions:1.0.0 (*)
+--- project :features:analytics
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- project :osiris (*)
|    +--- project :features:legacy (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:common (*)
|    +--- project :libraries:extensions (*)
|    +--- project :features:model (*)
|    +--- project :features:user-operations (*)
|    +--- project :libraries:local (*)
|    +--- project :dolap-lite:analytics
|    |    +--- project :shared-data
|    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- project :features:advertisingid (*)
|    |    +--- project :osiris (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- com.squareup.okhttp3:logging-interceptor:3.12.2 (*)
|    |    +--- com.google.android.gms:play-services-measurement-api:17.4.4
|    |    |    +--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    +--- com.google.android.gms:play-services-measurement-base:17.4.4
|    |    |    |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    +--- com.google.android.gms:play-services-measurement-impl:17.4.4
|    |    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    +--- com.google.android.gms:play-services-measurement-base:17.4.4 (*)
|    |    |    |    \--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-measurement-sdk-api:17.4.4
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    \--- com.google.android.gms:play-services-measurement-base:17.4.4 (*)
|    |    |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |    |    +--- com.google.firebase:firebase-installations:16.3.2 (*)
|    |    |    +--- com.google.firebase:firebase-installations-interop:16.0.0 (*)
|    |    |    \--- com.google.firebase:firebase-measurement-connector:18.0.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- com.adjust.sdk:adjust-android:4.21.0
|    |    +--- project :features:legacy (*)
|    |    +--- project :features:ab-test (*)
|    |    +--- project :features:configuration (*)
|    |    +--- com.trendyol.android-core:annotation:1.1.0
|    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
|    |    |    \--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- com.squareup.retrofit2:converter-gson:2.5.0 (*)
|    |    +--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
|    |    +--- com.google.firebase:firebase-analytics:17.4.4
|    |    |    +--- com.google.android.gms:play-services-measurement:17.4.4
|    |    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    +--- com.google.android.gms:play-services-measurement-base:17.4.4 (*)
|    |    |    |    +--- com.google.android.gms:play-services-measurement-impl:17.4.4 (*)
|    |    |    |    \--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-measurement-api:17.4.4 (*)
|    |    |    \--- com.google.android.gms:play-services-measurement-sdk:17.4.4
|    |    |         +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |         +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |         +--- com.google.android.gms:play-services-measurement-base:17.4.4 (*)
|    |    |         \--- com.google.android.gms:play-services-measurement-impl:17.4.4 (*)
|    |    +--- com.google.firebase:firebase-messaging:20.2.3
|    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    +--- com.google.android.datatransport:transport-api:2.2.0
|    |    |    +--- com.google.android.datatransport:transport-backend-cct:2.2.0 -> 2.2.3 (*)
|    |    |    +--- com.google.android.datatransport:transport-runtime:2.2.0 -> 2.2.3 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    +--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |    |    +--- com.google.firebase:firebase-datatransport:17.0.3
|    |    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    |    +--- com.google.android.datatransport:transport-api:2.1.0 -> 2.2.0
|    |    |    |    +--- com.google.android.datatransport:transport-backend-cct:2.1.0 -> 2.2.3 (*)
|    |    |    |    +--- com.google.android.datatransport:transport-runtime:2.1.0 -> 2.2.3 (*)
|    |    |    |    \--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    +--- com.google.firebase:firebase-encoders-json:16.0.0 -> 16.1.0 (*)
|    |    |    +--- com.google.firebase:firebase-iid:20.2.3 (*)
|    |    |    +--- com.google.firebase:firebase-installations:16.3.2 (*)
|    |    |    +--- com.google.firebase:firebase-installations-interop:16.0.0 (*)
|    |    |    \--- com.google.firebase:firebase-measurement-connector:18.0.0 (*)
|    |    +--- com.google.firebase:firebase-auth:19.3.2
|    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |    |    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-base:17.1.0 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    |    +--- com.google.firebase:firebase-auth-interop:19.0.0
|    |    |    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    |    |    \--- com.google.firebase:firebase-common:19.0.0 -> 19.3.0 (*)
|    |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    \--- com.google.firebase:firebase-components:16.0.0 (*)
|    |    +--- com.google.firebase:firebase-config:19.2.0
|    |    |    +--- com.google.android.gms:play-services-tasks:17.0.2 (*)
|    |    |    +--- com.google.firebase:firebase-abt:19.1.0
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |    |    |    +--- com.google.firebase:firebase-measurement-connector:18.0.0 (*)
|    |    |    |    \--- com.google.protobuf:protobuf-javalite:3.11.0
|    |    |    +--- com.google.firebase:firebase-common:19.3.0 (*)
|    |    |    +--- com.google.firebase:firebase-components:16.0.0 (*)
|    |    |    +--- com.google.firebase:firebase-installations:16.3.2 (*)
|    |    |    +--- com.google.firebase:firebase-installations-interop:16.0.0 (*)
|    |    |    +--- com.google.firebase:firebase-measurement-connector:18.0.0 (*)
|    |    |    \--- com.google.protobuf:protobuf-javalite:3.11.0
|    |    +--- com.google.android.gms:play-services-tagmanager:17.0.0
|    |    |    +--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-analytics-impl:17.0.0
|    |    |    |    +--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    |    \--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    +--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    |    \--- com.google.android.gms:play-services-tagmanager-api:17.0.0
|    |    |         +--- com.google.android.gms:play-services-analytics-impl:17.0.0 (*)
|    |    |         +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |         +--- com.google.android.gms:play-services-measurement:17.0.0 -> 17.4.4 (*)
|    |    |         +--- com.google.android.gms:play-services-measurement-api:17.0.0 -> 17.4.4 (*)
|    |    |         +--- com.google.android.gms:play-services-measurement-impl:17.0.0 -> 17.4.4 (*)
|    |    |         +--- com.google.android.gms:play-services-measurement-sdk:17.0.0 -> 17.4.4 (*)
|    |    |         \--- com.google.firebase:firebase-analytics:17.0.0 -> 17.4.4 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    +--- project :dolap-lite:data:remote-data
|    |    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    |    +--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    |    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    +--- project :dolap-lite:authentication:authentication-local
|    |    |    |    +--- project :dolap-lite:data:local-data
|    |    |    |    |    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    |    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    |    |    +--- javax.inject:javax.inject:1
|    |    |    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    |    |    +--- androidx.room:room-rxjava2:2.2.3 (*)
|    |    |    |    |    +--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
|    |    |    |    |    \--- androidx.sqlite:sqlite:2.1.0 (*)
|    |    |    |    +--- javax.inject:javax.inject:1
|    |    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    +--- com.squareup.okhttp3:logging-interceptor:3.12.2 (*)
|    |    |    +--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
|    |    |    +--- com.squareup.retrofit2:converter-gson:2.5.0 (*)
|    |    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    |    +--- com.squareup.okio:okio:1.15.0 -> 2.2.2 (*)
|    |    |    \--- com.github.chuckerteam.chucker:library:3.2.0 (*)
|    |    \--- com.trendyol.android-core:reporter:1.1.0 (*)
|    +--- project :dolap-lite:common
|    |    +--- project :osiris (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    +--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0
|    |    |    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    |    |    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    |    |    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    |    |    \--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    |    +--- androidx.databinding:databinding-runtime:3.6.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- com.google.dagger:dagger-android:2.26 (*)
|    |    +--- com.trendyol.android-core:base:1.0.4 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- project :dolap-lite:analytics (*)
|    |    +--- project :dolap-lite:address:address-communication
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    |    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    |    \--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
|    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    +--- com.google.dagger:dagger-android-support:2.26 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    \--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.squareup.retrofit2:converter-gson:2.5.0 (*)
|    +--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android-support:2.26 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- com.trendyol.android-core:reporter:1.1.0 (*)
|    +--- com.facebook.android:facebook-core:7.1.0
|    |    +--- com.parse.bolts:bolts-android:1.4.0
|    |    |    +--- com.parse.bolts:bolts-tasks:1.4.0
|    |    |    \--- com.parse.bolts:bolts-applinks:1.4.0
|    |    |         \--- com.parse.bolts:bolts-tasks:1.4.0
|    |    +--- androidx.annotation:annotation:1.1.0
|    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    \--- com.android.installreferrer:installreferrer:1.0
|    +--- com.facebook.android:facebook-android-sdk:7.1.0
|    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    +--- com.facebook.android:facebook-common:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    +--- androidx.legacy:legacy-support-v4:1.0.0
|    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    +--- androidx.media:media:1.0.0
|    |    |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    |    \--- androidx.versionedparcelable:versionedparcelable:1.0.0 -> 1.1.0 (*)
|    |    |    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    |    |    +--- androidx.legacy:legacy-support-core-ui:1.0.0
|    |    |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    |    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    |    |    |    +--- androidx.customview:customview:1.0.0 (*)
|    |    |    |    |    +--- androidx.viewpager:viewpager:1.0.0 (*)
|    |    |    |    |    +--- androidx.coordinatorlayout:coordinatorlayout:1.0.0 -> 1.1.0 (*)
|    |    |    |    |    +--- androidx.drawerlayout:drawerlayout:1.0.0 (*)
|    |    |    |    |    +--- androidx.slidingpanelayout:slidingpanelayout:1.0.0
|    |    |    |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    |    |    \--- androidx.customview:customview:1.0.0 (*)
|    |    |    |    |    +--- androidx.interpolator:interpolator:1.0.0 (*)
|    |    |    |    |    +--- androidx.swiperefreshlayout:swiperefreshlayout:1.0.0 -> 1.1.0
|    |    |    |    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    |    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    |    |    |    |    |    \--- androidx.interpolator:interpolator:1.0.0 (*)
|    |    |    |    |    +--- androidx.asynclayoutinflater:asynclayoutinflater:1.0.0
|    |    |    |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    |    |    \--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    |    \--- androidx.cursoradapter:cursoradapter:1.0.0 (*)
|    |    |    |    \--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    |    +--- androidx.browser:browser:1.0.0
|    |    |    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    |    |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|    |    |    |    +--- androidx.interpolator:interpolator:1.0.0 (*)
|    |    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    |    \--- androidx.legacy:legacy-support-core-ui:1.0.0 (*)
|    |    |    \--- com.google.zxing:core:3.3.3
|    |    +--- com.facebook.android:facebook-login:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    +--- com.facebook.android:facebook-common:7.1.0 (*)
|    |    |    \--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- com.facebook.android:facebook-share:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    +--- com.facebook.android:facebook-common:7.1.0 (*)
|    |    |    \--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- com.facebook.android:facebook-places:7.1.0
|    |    |    \--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    +--- com.facebook.android:facebook-applinks:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    +--- com.parse.bolts:bolts-android:1.4.0 (*)
|    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    \--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    |    +--- com.facebook.android:facebook-messenger:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    \--- com.parse.bolts:bolts-android:1.4.0 (*)
|    |    +--- com.facebook.android:facebook-gamingservices:7.1.0
|    |    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    |    +--- com.facebook.android:facebook-common:7.1.0 (*)
|    |    |    \--- com.facebook.android:facebook-share:7.1.0 (*)
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.31 -> 1.4.0 (*)
|    +--- com.adjust.sdk:adjust-android:4.21.0
|    \--- com.salesforce.marketingcloud:marketingcloudsdk:7.1.0
|         +--- com.google.firebase:firebase-messaging:20.1.0 -> 20.2.3 (*)
|         +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.50 -> 1.4.0 (*)
|         +--- androidx.annotation:annotation:1.1.0
|         +--- androidx.core:core:1.2.0 (*)
|         +--- androidx.collection:collection:1.1.0 (*)
|         +--- androidx.fragment:fragment:1.2.1 (*)
|         +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|         \--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
+--- project :features:seller-review
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:user-operations (*)
|    +--- project :libraries:extensions (*)
|    +--- project :features:common (*)
|    +--- project :libraries:local (*)
|    +--- project :features:order-detail
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-livedata:2.2.0 (*)
|    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    \--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- project :features:base
|    |    +--- project :features:common (*)
|    |    +--- project :features:analytics (*)
|    |    +--- project :libraries:extensions (*)
|    |    +--- project :osiris (*)
|    |    +--- project :libraries:trace
|    |    |    +--- project :libraries:remote (*)
|    |    |    +--- project :features:ab-test (*)
|    |    |    +--- project :features:configuration (*)
|    |    |    +--- com.newrelic.agent.android:android-agent:5.27.1
|    |    |    +--- androidx.annotation:annotation:1.1.0
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    \--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- project :dolap-lite:common (*)
|    |    +--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
|    |    +--- com.trendyol.android-core:reporter:1.1.0 (*)
|    |    +--- com.adjust.sdk:adjust-android:4.21.0
|    |    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    |    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    |    +--- com.roughike:bottom-bar:2.3.1
|    |    |    +--- androidx.appcompat:appcompat:1.0.0 -> 1.1.0 (*)
|    |    |    \--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
|    |    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- com.google.dagger:dagger-android-support:2.26 (*)
|    |    \--- com.google.dagger:dagger-android:2.26 (*)
|    +--- project :features:analytics (*)
|    +--- project :features:legacy (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3
|    |    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.1.0 (*)
|    |    \--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    \--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- project :features:order-detail (*)
+--- project :features:base (*)
+--- project :libraries:trace (*)
+--- project :features:authentication
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :features:common (*)
|    +--- project :features:analytics (*)
|    +--- project :libraries:extensions (*)
|    +--- project :osiris (*)
|    +--- project :libraries:trace (*)
|    +--- project :libraries:local (*)
|    +--- project :libraries:remote (*)
|    +--- project :features:configuration (*)
|    +--- project :features:user-operations (*)
|    +--- project :features:segmented-user
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- project :features:legacy (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    \--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- project :features:base (*)
|    +--- project :features:contracts
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- project :features:legacy (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    \--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- project :dolap-lite:common (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.facebook.android:facebook-core:7.1.0 (*)
|    +--- com.facebook.android:facebook-common:7.1.0 (*)
|    +--- com.salesforce.marketingcloud:marketingcloudsdk:7.1.0 (*)
|    +--- com.google.android.gms:play-services-auth:17.0.0
|    |    +--- androidx.fragment:fragment:1.0.0 -> 1.2.1 (*)
|    |    +--- androidx.loader:loader:1.0.0 (*)
|    |    +--- com.google.android.gms:play-services-auth-api-phone:17.0.0 -> 17.4.0
|    |    |    +--- com.google.android.gms:play-services-base:17.1.0 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.1.0 -> 17.2.1 (*)
|    |    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    +--- com.google.android.gms:play-services-auth-base:17.0.0
|    |    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- androidx.appcompat:appcompat-resources:1.1.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- com.facebook.shimmer:shimmer:0.5.0 (*)
|    \--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- project :features:segmented-user (*)
+--- project :features:contracts (*)
+--- project :features:address:ui
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :features:address:operations (*)
|    +--- project :features:base (*)
|    +--- project :features:common (*)
|    +--- project :libraries:extensions (*)
|    +--- project :features:scheduled-delivery
|    |    +--- project :libraries:local (*)
|    |    +--- project :features:configuration (*)
|    |    +--- project :features:user-operations (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    |    +--- project :features:address:operations (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    |    \--- com.trendyol.android-core:reporter:1.1.0 (*)
|    +--- project :features:analytics (*)
|    +--- project :features:authentication (*)
|    +--- project :dolap-lite:common (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.trendyol.android-core:reporter:1.1.0 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    \--- com.jakewharton.rxbinding3:rxbinding-recyclerview:3.1.0
|         +--- io.reactivex.rxjava2:rxandroid:2.1.1 (*)
|         +--- com.jakewharton.rxbinding3:rxbinding:3.1.0
|         |    +--- androidx.annotation:annotation:1.0.0 -> 1.1.0
|         |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.41 -> 1.4.0 (*)
|         |    +--- io.reactivex.rxjava2:rxjava:2.2.10 -> 2.2.17 (*)
|         |    \--- io.reactivex.rxjava2:rxandroid:2.1.1 (*)
|         +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|         \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.41 -> 1.4.0 (*)
+--- project :libraries:image-loader
|    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- com.github.bumptech.glide:annotations:4.10.0 -> 4.11.0
|    +--- com.github.bumptech.glide:okhttp3-integration:4.10.0
|    +--- project :features:configuration (*)
|    +--- project :libraries:remote (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    \--- com.trendyol.android-core:view-extensions:1.0.0 (*)
+--- project :libraries:image-viewer
|    +--- project :features:base (*)
|    +--- project :features:analytics (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :features:legacy (*)
|    +--- project :features:common (*)
|    +--- project :features:configuration (*)
|    +--- project :libraries:remote (*)
|    +--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    +--- com.github.bumptech.glide:annotations:4.10.0 -> 4.11.0
|    +--- com.github.bumptech.glide:okhttp3-integration:4.10.0
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- com.commit451:PhotoView:1.2.4
|    |    \--- androidx.legacy:legacy-support-v4:1.0.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    \--- com.google.dagger:dagger-android:2.26 (*)
+--- project :libraries:boutique-count-down-view (*)
+--- project :shared-data (*)
+--- project :libraries:card-operations
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- project :libraries:remote (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    \--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
+--- project :features:selectiondialog
|    +--- project :dolap-lite:common (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19
|    |    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.1.0 (*)
|    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    \--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
|    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- project :libraries:showcase-data
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
+--- project :dolap-lite:ui-components (*)
+--- project :dolap-lite:common (*)
+--- project :dolap-lite:product-detail
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :dolap-lite:paging
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    \--- javax.inject:javax.inject:1
|    +--- project :dolap-lite:data:content
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- project :dolap-lite:deep-link
|    |    +--- project :libraries:remote (*)
|    |    +--- project :features:user-operations (*)
|    |    +--- project :libraries:deeplink-dispatcher (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- project :dolap-lite:common (*)
|    |    +--- project :features:legacy (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    \--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- project :dolap-lite:authentication:authentication-domain
|    |    +--- project :dolap-lite:authentication:authentication-local (*)
|    |    +--- project :dolap-lite:authentication:authentication-remote
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- project :dolap-lite:data:local-data (*)
|    |    +--- project :shared-data (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- project :dolap-lite:deep-link (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    \--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- project :dolap-lite:filters
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- project :dolap-lite:ui-components (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    |    \--- com.google.android.material:material:1.1.0 (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- project :osiris (*)
|    +--- project :features:configuration (*)
|    +--- project :dolap-lite:favorite-operations
|    |    +--- project :dolap-lite:authentication:authentication-domain (*)
|    |    +--- project :dolap-lite:paging (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- project :dolap-lite:product
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    +--- project :libraries:extensions (*)
|    |    |    \--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- project :dolap-lite:analytics (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- project :libraries:extensions (*)
|    |    +--- project :osiris (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    \--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.trendyol.android-core:status:1.0.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- javax.inject:javax.inject:1
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- de.hdodenhof:circleimageview:2.2.0
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- com.github.Trendyol:android-ui-components:rating-bar-1.0.2
|    |    +--- androidx.databinding:databinding-common:3.5.2 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.5.2 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.5.2 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.50 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.50 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    \--- androidx.core:core-ktx:1.1.0 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- com.github.Trendyol.android-ui-components:image-slider:image-slider-1.0.6
|    |    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.1.0 (*)
|    |    +--- com.github.MertNYuksel:CircleIndicator:2a2e973374 (*)
|    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    +--- com.github.bumptech.glide:glide:4.10.0 -> 4.11.0 (*)
|    |    \--- com.github.Trendyol.android-ui-components:touch-delegator:image-slider-1.0.6 -> touch-delegator-1.0.0 (*)
|    +--- androidx.coordinatorlayout:coordinatorlayout:1.1.0 (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :libraries:image-viewer (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- project :dolap-lite:authentication:authentication-remote (*)
|    +--- project :libraries:remote (*)
|    +--- project :libraries:extensions (*)
|    +--- project :features:model (*)
|    +--- project :dolap-lite:favorite-listing
|    |    +--- project :dolap-lite:authentication:authentication-domain (*)
|    |    +--- project :dolap-lite:favorite-operations (*)
|    |    +--- project :dolap-lite:common (*)
|    |    +--- project :dolap-lite:paging (*)
|    |    +--- project :dolap-lite:product-card
|    |    |    +--- project :dolap-lite:ui-components (*)
|    |    |    +--- project :dolap-lite:favorite-operations (*)
|    |    |    +--- project :dolap-lite:product (*)
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    |    +--- project :libraries:extensions (*)
|    |    |    +--- com.trendyol.android-core:base:1.0.4 (*)
|    |    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    |    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    |    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    |    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    |    +--- project :dolap-lite:product (*)
|    |    +--- project :osiris (*)
|    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    |    +--- com.trendyol.android-core:status:1.0.0 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    |    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- com.google.dagger:dagger-android:2.26 (*)
|    |    +--- com.trendyol.android-core:base:1.0.4 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- project :dolap-lite:ui-components (*)
|    |    +--- project :dolap-lite:analytics (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- project :libraries:extensions (*)
|    |    +--- project :features:common (*)
|    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    +--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    \--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    +--- project :dolap-lite:dolaplite-homepage
|    |    +--- project :dolap-lite:authentication:authentication-domain (*)
|    |    +--- project :dolap-lite:common (*)
|    |    +--- project :dolap-lite:ui-components (*)
|    |    +--- project :dolap-lite:analytics (*)
|    |    +--- project :dolap-lite:paging (*)
|    |    +--- project :dolap-lite:product (*)
|    |    +--- project :dolap-lite:deep-link (*)
|    |    +--- project :osiris (*)
|    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- com.trendyol.android-core:status:1.0.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- com.google.dagger:dagger-android:2.26 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    |    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    |    +--- com.google.android.material:material:1.1.0 (*)
|    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    +--- project :dolap-lite:product-card (*)
|    |    +--- project :dolap-lite:search:search-suggestion
|    |    |    +--- project :dolap-lite:common (*)
|    |    |    +--- project :dolap-lite:ui-components (*)
|    |    |    +--- project :dolap-lite:search:search-data
|    |    |    |    +--- project :dolap-lite:paging (*)
|    |    |    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    |    |    +--- javax.inject:javax.inject:1
|    |    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    |    |    +--- project :dolap-lite:data:remote-data (*)
|    |    |    |    +--- project :dolap-lite:filters (*)
|    |    |    |    +--- project :dolap-lite:analytics (*)
|    |    |    |    +--- project :dolap-lite:product (*)
|    |    |    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    |    |    \--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    |    |    +--- javax.inject:javax.inject:1
|    |    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    |    +--- com.google.dagger:dagger-android:2.26 (*)
|    |    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    |    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    |    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    |    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    |    +--- androidx.databinding:databinding-common:4.0.1
|    |    |    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    |    |    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    |    |    +--- project :dolap-lite:filters (*)
|    |    |    +--- project :dolap-lite:data:remote-data (*)
|    |    |    +--- project :dolap-lite:analytics (*)
|    |    |    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    |    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    |    +--- com.trendyol.android-core:base:1.0.4 (*)
|    |    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    |    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    |    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    |    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- project :dolap-lite:filters (*)
|    |    +--- project :dolap-lite:favorite-operations (*)
|    |    +--- project :libraries:extensions (*)
|    |    +--- project :features:model (*)
|    |    +--- project :libraries:remote (*)
|    |    +--- project :libraries:widgets (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    |    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    |    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    |    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    |    +--- com.trendyol.android-core:base:1.0.4 (*)
|    |    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    |    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    |    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    |    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    |    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    |    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    |    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    +--- project :dolap-lite:product (*)
|    +--- project :dolap-lite:product-card (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- androidx.appcompat:appcompat-resources:1.1.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    \--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- project :dolap-lite:checkout
|    +--- project :dolap-lite:common (*)
|    +--- project :shared-data (*)
|    +--- project :dolap-lite:address:address-data
|    |    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    |    +--- javax.inject:javax.inject:1
|    |    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    |    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    |    +--- project :dolap-lite:data:remote-data (*)
|    |    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    |    \--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :dolap-lite:address:address-communication (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- project :libraries:card-operations (*)
|    +--- project :osiris (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.trendyol.android-core:status:1.0.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :features:selectiondialog (*)
|    +--- project :libraries:extensions (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.google.dagger:dagger-android-support:2.26 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- project :dolap-lite:address:address-ui
|    +--- project :dolap-lite:address:address-communication (*)
|    +--- project :dolap-lite:address:address-data (*)
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- com.github.Trendyol.android-ui-components:phonenumber:phonenumber-1.0.2
|    |    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.1.0 (*)
|    |    \--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
|    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- androidx.appcompat:appcompat-resources:1.1.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- project :dolap-lite:address:address-data (*)
+--- project :dolap-lite:address:address-communication (*)
+--- project :dolap-lite:dolaplite-homepage (*)
+--- project :dolap-lite:deep-link (*)
+--- project :dolap-lite:orders
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :dolap-lite:paging (*)
|    +--- project :dolap-lite:deep-link (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- com.squareup.retrofit2:retrofit:2.5.0 (*)
|    +--- com.trendyol.android-core:status:1.0.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- project :dolap-lite:product (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- com.github.Trendyol:android-ui-components:rating-bar-1.0.2 (*)
|    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    \--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- project :dolap-lite:search:search-suggestion (*)
+--- project :dolap-lite:search:search-ui
|    +--- project :dolap-lite:authentication:authentication-domain (*)
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:filters (*)
|    +--- project :dolap-lite:search:search-data (*)
|    +--- project :dolap-lite:ui-components (*)
|    +--- project :dolap-lite:paging (*)
|    +--- project :dolap-lite:deep-link (*)
|    +--- project :osiris (*)
|    +--- project :dolap-lite:product (*)
|    +--- com.trendyol.android-core:status:1.0.0 (*)
|    +--- com.trendyol.android-core:resource:1.0.3 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- com.github.Trendyol:StateLayout:1.4.4 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    +--- de.hdodenhof:circleimageview:2.2.0
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- com.google.android.material:material:1.1.0 (*)
|    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.databinding:databinding-common:4.0.1
|    +--- androidx.databinding:databinding-runtime:4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :dolap-lite:product-card (*)
|    +--- project :dolap-lite:search:search-suggestion (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- project :dolap-lite:favorite-operations (*)
|    +--- project :features:model (*)
|    +--- project :libraries:remote (*)
|    +--- project :libraries:extensions (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- project :libraries:showcase-data (*)
|    +--- com.github.Trendyol:showcase:0.8
|    |    +--- androidx.databinding:databinding-common:3.4.2 -> 4.0.1
|    |    +--- androidx.databinding:databinding-runtime:3.4.2 -> 4.0.1 (*)
|    |    +--- androidx.databinding:databinding-adapters:3.4.2 -> 4.0.1 (*)
|    |    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.41 -> 1.4.0 (*)
|    |    +--- androidx.appcompat:appcompat:1.0.2 -> 1.1.0 (*)
|    |    +--- androidx.cardview:cardview:1.0.0 (*)
|    |    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    |    +--- com.github.bumptech.glide:glide:4.11.0 (*)
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.41 -> 1.4.0 (*)
|    +--- com.trendyol.android-core:android-extensions:1.0.7 (*)
|    +--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
|    +--- com.trendyol.android-core:base:1.0.4 (*)
|    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
|    +--- com.trendyol.android-core:view-extensions:1.0.0 (*)
|    +--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
|    +--- androidx.drawerlayout:drawerlayout:1.0.0 (*)
|    \--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- project :dolap-lite:search:search-data (*)
+--- project :dolap-lite:analytics (*)
+--- project :dolap-lite:authentication:authentication-domain (*)
+--- project :dolap-lite:authentication:authentication-remote (*)
+--- project :dolap-lite:data:local-data (*)
+--- project :dolap-lite:data:remote-data (*)
+--- project :dolap-lite:data:content (*)
+--- project :dolap-lite:authentication:authentication-local (*)
+--- project :dolap-lite:filters (*)
+--- project :dolap-lite:paging (*)
+--- project :dolap-lite:favorite-operations (*)
+--- project :dolap-lite:favorite-listing (*)
+--- project :dolap-lite:product-card (*)
+--- project :dolap-lite:product (*)
+--- project :dolap-lite:dolap-lite
|    +--- project :dolap-lite:common (*)
|    +--- project :dolap-lite:analytics (*)
|    +--- project :dolap-lite:authentication:authentication-domain (*)
|    +--- project :libraries:deeplink-dispatcher (*)
|    +--- project :osiris (*)
|    +--- project :shared-data (*)
|    +--- javax.inject:javax.inject:1
|    +--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
|    +--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
|    +--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- project :dolap-lite:product-detail (*)
|    +--- project :dolap-lite:checkout (*)
|    +--- project :dolap-lite:address:address-ui (*)
|    +--- project :dolap-lite:dolaplite-homepage (*)
|    +--- project :dolap-lite:deep-link (*)
|    +--- project :dolap-lite:orders (*)
|    +--- project :dolap-lite:search:search-suggestion (*)
|    +--- project :dolap-lite:search:search-ui (*)
|    +--- project :dolap-lite:data:local-data (*)
|    +--- project :dolap-lite:favorite-listing (*)
|    +--- project :dolap-lite:favorite-operations (*)
|    +--- project :dolap-lite:data:remote-data (*)
|    +--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- com.github.MertNYuksel:CircleIndicator:2a2e973374 (*)
|    +--- com.github.Trendyol.android-ui-components:image-slider:image-slider-1.0.6 (*)
|    +--- com.github.Trendyol:medusa:0.9.1-rc (*)
|    +--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
|    +--- com.trendyol.android-core:annotation:1.1.0 (*)
|    +--- com.google.code.gson:gson:2.8.5 -> 2.8.6
|    \--- com.trendyol.android-core:resource:1.0.3 (*)
+--- project :instant-delivery:local
|    +--- javax.inject:javax.inject:1
|    +--- com.google.dagger:dagger:2.26 -> 2.27 (*)
|    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
|    +--- androidx.room:room-rxjava2:2.2.3 (*)
|    +--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
|    \--- androidx.sqlite:sqlite:2.1.0 (*)
+--- project :features:scheduled-delivery (*)
+--- project :meal:local
|    +--- androidx.room:room-rxjava2:2.2.3 (*)
|    +--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
|    +--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib:1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0 (*)
|    +--- androidx.core:core:1.1.0 -> 1.2.0 (*)
|    +--- com.google.dagger:dagger-android-support:2.26 (*)
|    +--- com.google.dagger:dagger-android:2.26 (*)
|    \--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
+--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
+--- com.google.dagger:dagger:2.26 -> 2.27 (*)
+--- com.google.dagger:dagger-android:2.26 (*)
+--- com.google.dagger:dagger-android-support:2.26 (*)
+--- com.trendyol.android-core:base:1.0.4 (*)
+--- com.trendyol.android-core:android-extensions:1.0.7 (*)
+--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
+--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
+--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
+--- javax.inject:javax.inject:1
+--- androidx.appcompat:appcompat:1.1.0 (*)
+--- androidx.core:core:1.1.0 -> 1.2.0 (*)
+--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
+--- androidx.browser:browser:1.0.0 (*)
+--- androidx.appcompat:appcompat-resources:1.1.0 (*)
+--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
+--- com.google.android.material:material:1.1.0 (*)
+--- androidx.cardview:cardview:1.0.0 (*)
+--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
+--- androidx.transition:transition:1.2.0 (*)
+--- com.google.firebase:firebase-common:19.3.0 (*)
+--- com.google.firebase:firebase-messaging:20.2.3 (*)
+--- com.google.firebase:firebase-appindexing:19.1.0
|    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    +--- com.google.android.gms:play-services-base:17.1.0 (*)
|    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    \--- com.google.firebase:firebase-common:19.3.0 (*)
+--- com.google.firebase:firebase-auth:19.3.2 (*)
+--- com.google.firebase:firebase-config:19.2.0 (*)
+--- com.google.firebase:firebase-iid:20.2.3 (*)
+--- com.google.android.gms:play-services-auth:17.0.0 (*)
+--- com.google.android.gms:play-services-auth-api-phone:17.4.0 (*)
+--- com.google.android.gms:play-services-gcm:17.0.0
|    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    +--- androidx.legacy:legacy-support-core-utils:1.0.0 (*)
|    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    +--- com.google.android.gms:play-services-iid:17.0.0
|    |    +--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)
|    |    +--- androidx.core:core:1.0.0 -> 1.2.0 (*)
|    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    +--- com.google.android.gms:play-services-stats:17.0.0 (*)
|    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    \--- com.google.android.gms:play-services-stats:17.0.0 (*)
+--- com.google.android.play:core:1.6.3
+--- com.google.android.gms:play-services-maps:17.0.0 (*)
+--- com.google.android.gms:play-services-basement:17.2.1 (*)
+--- com.google.android.gms:play-services-measurement-api:17.4.4 (*)
+--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
+--- com.google.android.gms:play-services-iid:17.0.0 (*)
+--- com.google.android.gms:play-services-tasks:17.0.2 (*)
+--- com.google.android.gms:play-services-base:17.1.0 (*)
+--- com.google.firebase:firebase-crashlytics:17.1.0 (*)
+--- com.facebook.stetho:stetho:1.5.1 (*)
+--- com.newrelic.agent.android:android-agent:5.27.1
+--- com.github.arturogutierrez:badges:1.0.5
+--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- com.salesforce.marketingcloud:marketingcloudsdk:7.1.0 (*)
+--- com.facebook.android:facebook-core:7.1.0 (*)
+--- com.facebook.android:facebook-common:7.1.0 (*)
+--- com.facebook.android:facebook-applinks:7.1.0 (*)
+--- com.adjust.sdk:adjust-android:4.21.0
+--- com.adjust.sdk:adjust-android-criteo:4.21.0
+--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
+--- com.squareup.okhttp3:logging-interceptor:3.12.2 (*)
+--- com.google.code.gson:gson:2.8.5 -> 2.8.6
+--- com.squareup.retrofit2:retrofit:2.5.0 (*)
+--- com.squareup.retrofit2:converter-gson:2.5.0 (*)
+--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
+--- com.trendyol.android-core:resource:1.0.3 (*)
+--- com.trendyol.android-core:status:1.0.0 (*)
+--- com.trendyol.android-core:annotation:1.1.0 (*)
+--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
+--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
+--- com.jakewharton.rxbinding2:rxbinding:2.2.0 (*)
+--- com.commit451:PhotoView:1.2.4 (*)
+--- com.github.Trendyol:StateLayout:1.4.4 (*)
+--- com.roughike:bottom-bar:2.3.1 (*)
+--- com.beloo.widget:ChipsLayoutManager:0.3.7
+--- com.github.MertNYuksel:CircleIndicator:2a2e973374 (*)
+--- com.google.android:flexbox:1.1.0
+--- de.hdodenhof:circleimageview:2.2.0
+--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
+--- com.facebook.shimmer:shimmer:0.5.0 (*)
+--- com.github.erkutaras:impression:0.0.3 (*)
+--- com.github.Trendyol:showcase:0.8 (*)
+--- com.github.Trendyol:medusa:0.9.1-rc (*)
+--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
+--- com.github.Trendyol.android-ui-components:suggestion-input-view:suggestion-input-view-1.1.0
|    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.core:core-ktx:1.1.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.1.0 (*)
|    \--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
+--- com.github.Trendyol.android-ui-components:card-input-view:card-input-view-1.0.5
|    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    +--- androidx.core:core-ktx:1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    \--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
+--- com.github.Trendyol.android-ui-components:quantity-picker-view:quantity-picker-view-1.2.1
|    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.core:core-ktx:1.1.0 (*)
|    +--- com.google.android.material:material:1.0.0 -> 1.1.0 (*)
|    +--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
|    \--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
+--- com.github.Trendyol.android-ui-components:phonenumber:phonenumber-1.0.2 (*)
+--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
+--- com.github.Trendyol.android-ui-components:timeline-view:timeline-view-1.0.0
|    +--- androidx.databinding:databinding-common:3.5.0 -> 4.0.1
|    +--- androidx.databinding:databinding-runtime:3.5.0 -> 4.0.1 (*)
|    +--- androidx.databinding:databinding-adapters:3.5.0 -> 4.0.1 (*)
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    +--- androidx.core:core-ktx:1.1.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.1.0 (*)
|    \--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
+--- com.github.Trendyol.android-ui-components:fit-option-message-view:52e0cb60c8
|    +--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.3.61 -> 1.4.0 (*)
|    +--- org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.61 -> 1.4.0 (*)
|    +--- androidx.appcompat:appcompat:1.1.0 (*)
|    \--- androidx.core:core-ktx:1.1.0 (*)
+--- com.google.android.libraries.places:places:2.2.0
|    +--- androidx.appcompat:appcompat:1.0.0 -> 1.1.0 (*)
|    +--- androidx.cardview:cardview:1.0.0 (*)
|    +--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
|    +--- androidx.lifecycle:lifecycle-extensions:2.1.0 -> 2.2.0 (*)
|    +--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
|    +--- com.android.volley:volley:1.1.1
|    +--- com.google.android.datatransport:transport-api:2.1.0 -> 2.2.0
|    +--- com.google.android.datatransport:transport-backend-cct:2.1.0 -> 2.2.3 (*)
|    +--- com.google.android.datatransport:transport-runtime:2.1.0 -> 2.2.3 (*)
|    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    +--- com.google.android.gms:play-services-location:17.0.0
|    |    +--- com.google.android.gms:play-services-base:17.0.0 -> 17.1.0 (*)
|    |    +--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    +--- com.google.android.gms:play-services-places-placereport:17.0.0
|    |    |    \--- com.google.android.gms:play-services-basement:17.0.0 -> 17.2.1 (*)
|    |    \--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    +--- com.google.android.gms:play-services-maps:17.0.0 (*)
|    +--- com.google.android.gms:play-services-tasks:17.0.0 -> 17.0.2 (*)
|    +--- com.google.auto.value:auto-value-annotations:1.6.2 -> 1.6.5
|    \--- com.google.code.gson:gson:2.8.5 -> 2.8.6
+--- com.github.Trendyol.android-ui-components:image-slider:image-slider-1.0.6 (*)
+--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- androidx.swiperefreshlayout:swiperefreshlayout:1.1.0 (*)
+--- com.jakewharton.rxbinding3:rxbinding-recyclerview:3.1.0 (*)
+--- androidx.viewpager:viewpager:1.0.0 (*)
+--- androidx.viewpager2:viewpager2:1.0.0 (*)
+--- androidx.drawerlayout:drawerlayout:1.0.0 (*)
+--- androidx.coordinatorlayout:coordinatorlayout:1.1.0 (*)
+--- com.github.Trendyol:android-ui-components:rating-bar-1.0.2 (*)
+--- androidx.room:room-rxjava2:2.2.3 (*)
+--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
+--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
+--- androidx.sqlite:sqlite:2.1.0 (*)
+--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
+--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-process:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-livedata:2.2.0 (*)
+--- androidx.arch.core:core-common:2.1.0 (*)
+--- com.github.chuckerteam.chucker:library:3.2.0 (*)
+--- project :performance-noop
|    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
\--- com.squareup.leakcanary:leakcanary-android:2.0-alpha-2
     +--- com.squareup.leakcanary:leakcanary-android-core:2.0-alpha-2
     |    +--- com.squareup.leakcanary:leakcanary-analyzer:2.0-alpha-2
     |    |    +--- com.squareup.leakcanary:leakcanary-watcher:2.0-alpha-2
     |    |    |    +--- com.squareup.leakcanary:leakcanary-log:2.0-alpha-2
     |    |    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     |    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     |    |    +--- com.squareup.leakcanary:leakcanary-haha:2.0-alpha-2
     |    |    |    +--- com.squareup.leakcanary:leakcanary-log:2.0-alpha-2 (*)
     |    |    |    +--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     |    |    |    \--- com.squareup.okio:okio:2.2.2 (*)
     |    |    +--- androidx.annotation:annotation:1.0.2 -> 1.1.0
     |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     |    +--- com.squareup.leakcanary:leaksentry:2.0-alpha-2
     |    |    +--- com.squareup.leakcanary:leakcanary-watcher:2.0-alpha-2 (*)
     |    |    +--- androidx.core:core:1.0.1 -> 1.2.0 (*)
     |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     |    +--- androidx.annotation:annotation:1.0.2 -> 1.1.0
     |    +--- androidx.core:core:1.0.1 -> 1.2.0 (*)
     |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)
     \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)

(*) - dependencies omitted (listed previously)

A web-based, searchable dependency report is available by adding the --scan option.
"""

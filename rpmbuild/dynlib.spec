Name:           mon-application-lib
Version:        1.0.0
Release:        1%{?dist}
Summary:        Déploiement de librairies dynamiques pré-compilées
License:        Proprietary
Group:          Development/Libraries

Name:           mon-application-lib
Version:        1.0.0
Release:        1%{?dist}
Summary:        Déploiement de .so sans vérification de dépendances
License:        Proprietary



# --- DÉSACTIVATION DES DÉPENDANCES AUTOMATIQUES ---
AutoReqProv: no
# --------------------------------------------------

# Evite le nettoyage automatique
%define __spec_install_post /usr/lib/rpm/brp-compress
%define debug_package %{nil}


%description
Ce paquet installe des bibliothèques .so déjà compilées sans phase de build.

%prep
# Pas de code source à extraire, on peut laisser vide ou créer le répertoire
%setup -q -c -T

%build
# Rien à compiler ici.

%prep
# Pas de code source à extraire, on peut laisser vide ou créer le répertoire
%setup -q -c -T

%build
# Rien à compiler ici.

# Copie des fichiers .so depuis votre répertoire local vers le buildroot
# On suppose que les fichiers sont dans le même dossier que le .spec
install -m 755 %{_sourcedir}/libma-lib.so.1.0 %{buildroot}%{_libdir}/

# Création du lien symbolique (standard pour les .so)
ln -s libma-lib.so.1.0 %{buildroot}%{_libdir}/libma-lib.so.1
ln -s libma-lib.so.1 %{buildroot}%{_libdir}/libma-lib.so

%post
# Très important : on rafraîchit le cache de l'éditeur de liens dynamiques
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/libma-lib.so.1.0
%{_libdir}/libma-lib.so.1
%{_libdir}/libma-lib.so


%changelog
* Sun Mar 01 2026 Votre Nom <vous@exemple.com> - 1.0.0-1
- Initial release avec binaires pré-compilés
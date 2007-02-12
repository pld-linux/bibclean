# TODO:
# - patch Makefile to make clean build using DESTDIR
# - human-like bibcleanrc init file location
Summary:	BibTeX prettyprinter, portability verifier, and syntax checker
Summary(pl.UTF-8):   Narzędzie do ładnego drukowania, kontroli przenośności i składni BibTeXa
Name:		bibclean
Version:	2.11.4
Release:	4
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.math.utah.edu/pub/tex/bib/%{name}-%{version}.tar.bz2
# Source0-md5:	7fbcae38a6227831dccd6f147260b3dc
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.318
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BibTeX prettyprinter, portability verifier, and syntax checker. Some
other tools require that this be used before they operate, so they
don't have to parse arbitrary BibTeX.

%description -l pl.UTF-8
Narzędzie do ładnego drukowania, kontroli przenośności i składni
BibTeXa. Niektóre inne narzędzia wymagają tego przed użyciem, dzięki
czemu nie muszą przetwarzać dowolnego BibTeXa.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/env.d}

%{__make} install \
	CP="cp -p" \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

echo '#BIBCLEANEXT=.ini' > $RPM_BUILD_ROOT/etc/env.d/BIBCLEANEXT
echo '#BIBINPUTS=$PATH' > $RPM_BUILD_ROOT/etc/env.d/BIBINPUTS
# Will that work?
echo 'BIBCLEANINI=%{_sysconfdir}/bibcleanrc' > $RPM_BUILD_ROOT/etc/env.d/BIBCLEANINI

mv -f $RPM_BUILD_ROOT%{_bindir}/.bibcleanrc $RPM_BUILD_ROOT%{_sysconfdir}/bibcleanrc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%env_update

%postun
%env_update

%files
%defattr(644,root,root,755)
%doc ChangeLog README *.txt *.html *.pdf *.hlp *.bok *.org *.ltx *.eok
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bibcleanrc
%config(noreplace) %verify(not md5 mtime size) /etc/env.d/*
%{_mandir}/man1/*.1*

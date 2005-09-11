%include        /usr/lib/rpm/macros.perl
Summary:	Virtual web logfile rotater/parser
Summary(pl):	Narzêdzie do rotacji i parsowania logów z wirtualnych hostów
Name:		vlogger
Version:	1.3
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://n0rp.chemlab.org/vlogger/%{name}-%{version}.tar.gz
# Source0-md5:	4170a4bf7ab8b24373458e8ac820c0a1
Patch0:		%{name}-debian.patch
Patch1:		%{name}-vhost.patch
URL:		http://n0rp.chemlab.org/vlogger/
BuildRequires:	perl-TimeDate
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vlogger is a little piece of code borned to handle dealing with large
amounts of virtualhost logs. It's bad news that Apache can't do this
on its own. Vlogger takes piped input from Apache, splits it off to
separate files based on the first field. It uses a file handle cache
so it can't run out of file descriptors. It will also start a new
logfile every night at midnight, and maintain a symlink to the most
recent file. For security, it can drop privileges and do a chroot to
the logs directory.

%description -l pl
Vlogger to ma³y kawa³ek kodu stworzony do obs³ugi du¿ych ilo¶ci logów
z wirtualnych hostów. Apache niestety nie umie obs³ugiwaæ ich
samodzielnie. Vlogger pobiera w potoku dane z Apache'a i dzieli je na
poszczególne pliki bazuj±c na pierwszym polu. Wykorzystuje keszowanie
otwartych plików, wiêc nie przekroczy maksymalnej liczby deskryptorów
plików. Otwiera tak¿e nowy plik logów codziennie o pó³nocy i tworzy
dowi±zania symboliczne do ostatniego pliku. Ze wzglêdów bezpieczeñstwa
mo¿e zrzucaæ uprawnienia i chrootowaæ siê do katalogu logów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.conf *.sql
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*

EXTRA_DIST = \
	MATERIAL-NIX-Round \
	COPYING \
	AUTHORS \
	README.md

themedir = $(datadir)/icons

install-data-hook:
	$(MKDIR_P) $(DESTDIR)/usr/share/icons
	cp -Rv MATERIAL-NIX-Round $(DESTDIR)/usr/share/icons/.

uninstall-hook:
	test -e $(DESTDIR)/usr/share/icons/MATERIAL-NIX-Round && rm -rfv $(DESTDIR)/usr/share/icons/MATERIAL-NIX-Round

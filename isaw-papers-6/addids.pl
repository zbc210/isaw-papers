#! /usr/bin/perl
my $i = 0;
while (<>) {
    s/<p/"<p id=\"p" . $i++ . "\" "/e;
    print;
}

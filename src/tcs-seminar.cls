\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tcs-seminar}[2012/03/07 v1.1 Theoretical Computer Science Seminar]

\DeclareOption{draft}{\PassOptionsToClass{draft}{article}}
\DeclareOption{final}{\PassOptionsToClass{final}{article}}
\ProcessOptions\relax

\LoadClass[a4paper,twocolumn,10pt]{article}


%%% Grundlegendes
\RequirePackage{etex}
\RequirePackage{fixltx2e}
\RequirePackage{lmodern}
\RequirePackage[T1]{fontenc}
\RequirePackage[babel]{microtype}


%%% Layout
\RequirePackage[left=1.5cm,right=1.5cm,top=2cm,bottom=2cm]{geometry}
\RequirePackage{setspace}
\setstretch{1.1}
\RequirePackage{flushend}


% Abstract speichern
\newcommand{\abstract@error}{\ClassError{tcs-seminar}{%
    Using the abstract environment after \protect\maketitle\space is prohibited}{%
    Move the abstract environment to a position before the invocation of \protect\maketitle}}
\newsavebox{\box@abstract}
\newcommand*\@abstractlabel[1][\relax]{\normalfont\bfseries\abstractname\quad}%
\renewenvironment{abstract}{%
  \linewidth\textwidth\advance\linewidth-3cm%
  \global\setbox\box@abstract=\vbox\bgroup%
      \list{}{\topsep1ex%
           \labelsep\z@%
           \labelwidth\z@%
           \itemindent\z@%
           \rightmargin\z@%
           \leftmargin\z@%
           \let\makelabel\@abstractlabel}%
        \item\relax}%
  {\endlist\par\vskip.5ex\egroup}
  
% Titel & Abstract ausgeben
\RequirePackage{amssymb} % Für die Raute
\newcommand{\@fancyrule}[0]{\par%
  \rule[0.23\baselineskip]{0.3\textwidth}{0.4pt}%
  \hskip 4pt\(\blacklozenge\)\hskip 4pt%
  \rule[0.23\baselineskip]{0.3\textwidth}{0.4pt}\par}
\renewcommand{\@maketitle}{%
  \global\let\abstract\abstract@error%
  \global\let\endabstract\relax%
  \spacing{1.0}\center%
  \let \footnote \thanks
  {\sffamily\Huge \@title \par}%
  \vskip 3ex%
  {\sffamily\large
  \lineskip .5em%
  \begin{tabular}[t]{c}%
    \@author
  \end{tabular}}\par%
  \usebox\box@abstract%
  \@fancyrule\endspacing\endcenter}

% Überschriften
\renewcommand\section{\@startsection{section}{1}{\z@}%
    {-4mm \@plus -0.6ex \@minus -.2ex}%
    {2mm \@plus 0.2ex}%
    {\normalfont\raggedright\large\bfseries\sffamily}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
    {-4mm \@plus -0.3ex \@minus -.2ex}%
    {1mm \@plus 0.1ex}%
    {\normalfont\raggedright\bfseries\sffamily}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
    {-2mm \@plus -0.2ex \@minus -.2ex}%
    {1mm \@plus 0ex}%
    {\normalfont\raggedright\sffamily}}

